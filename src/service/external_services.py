import asyncio
import random


async def fetch_fraud_score(applicant_id: int):
    await asyncio.sleep(1)
    return {"fraud_probability": round(random.random(), 2)}


async def fetch_macro_risk():
    await asyncio.sleep(1)
    return {"macro_risk_index": round(random.uniform(0.1, 1.0), 2)}