import asyncio
from src.service.external_services import fetch_fraud_score, fetch_macro_risk


class RiskOrchestrator:

    async def enrich(self, applicant_id, base_result):

        results = await asyncio.gather(
            fetch_fraud_score(applicant_id),
            fetch_macro_risk()
        )

        for result in results:
            base_result.update(result)

        return base_result
