from pydantic import BaseModel, Field


class LoanRequest(BaseModel):
    age: int = Field(..., gt=18)
    income: float = Field(..., gt=0)
    loan_amount: float = Field(..., gt=0)
    credit_score: int = Field(..., ge=300, le=850)
    employment_years: int = Field(..., ge=0)
    city: str


class LoanResponse(BaseModel):
    loan_income_ratio: float
    risk_flag: str
    employment_score: float
    recommendation: str