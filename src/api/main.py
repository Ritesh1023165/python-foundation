import time
import logging
import uuid
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.api.schemas import LoanRequest, LoanResponse
from src.api.dependencies import get_risk_engine
from src.service.risk_engine import RiskEngine
from src.service.logging_config import setup_logging
from src.service.validator import LoanValidator
from src.service.audit_service import AuditService
from src.service.exceptions import ValidationError

setup_logging()
logger = logging.getLogger("loan-api")

app = FastAPI(title="Loan Risk Inference API")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 4)
    logger.info(
        f"{request.method} {request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {process_time}s"
    )
    return response

@app.post("/evaluate-risk", response_model=LoanResponse)
async def evaluate_risk(
    request: LoanRequest,
    engine: RiskEngine = Depends(get_risk_engine)
):
    try:
        correlation_id = uuid.uuid1()
        AuditService.log_request(request)
        LoanValidator.validate(request)
        result = engine.evaluate(request)
        AuditService.log_response(result)
        return result
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": str(exc)
        },
    )