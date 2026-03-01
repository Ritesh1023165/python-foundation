from src.service.exceptions import ValidationError
from src.service.logging_config import setup_logging

setup_logging()

class LoanValidator:  

    @staticmethod
    def validate(request):
        if request.loan_amount > request.income * 5:
            raise ValidationError("Loan amount too high compared to income")

        if request.credit_score < 300 or request.credit_score > 850:
            raise ValidationError("Invalid credit score range")