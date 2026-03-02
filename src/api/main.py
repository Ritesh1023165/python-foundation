import time
import logging
from typing import Any
import uuid
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.api.schemas import LoanRequest, LoanResponse
from src.api.dependencies import get_risk_engine, get_risk_orchestrator
from src.service.risk_engine import RiskEngine
from src.service.logging_config import setup_logging
from src.service.validator import LoanValidator
from src.service.audit_service import AuditService
from src.service.exceptions import ValidationError
from src.service.orchestrator import RiskOrchestrator
from src.middleware.correlation import add_correlation_id, get_cid

setup_logging()
logger = logging.getLogger("loan-api")

app = FastAPI(title="Loan Risk Inference API")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 4)
    logger.info(
        f"Correlation-ID: {request.state.correlation_id} "
        f"{request.method} {request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {process_time}s"
    )
    return response

app.middleware("http")(add_correlation_id)

@app.post("/evaluate-risk")
async def evaluate_risk(
    request: LoanRequest,
    engine: RiskEngine = Depends(get_risk_engine),
    orchestrator: RiskOrchestrator = Depends(get_risk_orchestrator),
    cid: str = Depends(get_cid)
):
    try:
        AuditService.log_request(request, cid)
        LoanValidator.validate(request)
        result = engine.evaluate(request)
        enriched_result = await orchestrator.enrich(applicant_id=1, base_result=result)
        if enriched_result["fraud_probability"] > 0.7:
            enriched_result["recommendation"] = "Manual Review Required"
        AuditService.log_response(enriched_result, cid)
        return wrap_response(enriched_result, cid)
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)} | Correlation-ID: {getattr(request.state, "correlation_id", "unknown")}")

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "correlation_id": getattr(request.state, "correlation_id", "unknown"),
            "error": "Internal Server Error",
            "detail": str(exc)
        },
    )

def wrap_response(data: Any = None, cid: Any = None) -> dict:
    return {
        "status": "success",
        "correlation_id": cid,
        "data": data
    }