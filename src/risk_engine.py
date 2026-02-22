import numpy as np


class RiskEngine:

    def evaluate(self, request):
        loan_income_ratio = request.loan_amount / request.income
        employment_score = np.log1p(request.employment_years)

        if request.credit_score < 600:
            risk_flag = "high"
            recommendation = "Reject"
        elif request.credit_score < 700:
            risk_flag = "medium"
            recommendation = "Approve with caution"
        else:
            risk_flag = "low"
            recommendation = "Approve"

        return {
            "loan_income_ratio": round(loan_income_ratio, 2),
            "risk_flag": risk_flag,
            "employment_score": round(employment_score, 2),
            "recommendation": recommendation
        }