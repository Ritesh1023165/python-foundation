from fastapi import FastAPI, Depends
from src.api.schemas import LoanRequest, LoanResponse
from src.api.dependencies import get_risk_engine
from src.risk_engine import RiskEngine


app = FastAPI(title="Loan Risk Inference API")


@app.post("/evaluate-risk", response_model=LoanResponse)
async def evaluate_risk(
    request: LoanRequest,
    engine: RiskEngine = Depends(get_risk_engine)
):
    result = engine.evaluate(request)
    return result