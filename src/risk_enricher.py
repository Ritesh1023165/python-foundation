import asyncio
from async_services import (
    fetch_credit_risk,
    fetch_fraud_score,
    fetch_macro_risk
)


async def enrich_applicant(applicant_id: int):
    results = await asyncio.gather(
        fetch_credit_risk(applicant_id),
        fetch_fraud_score(applicant_id),
        fetch_macro_risk()
    )
    print("Fetch initiated")
    enriched_data = {}
    for result in results:
        enriched_data.update(result)

    return enriched_data