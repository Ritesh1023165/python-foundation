import asyncio
import random

async def fetch_credit_risk(applicant_id: int):
    await asyncio.sleep(1.0)  # Simulate API delay
    return {"credit_risk_score": random.randint(300, 850)}


async def fetch_fraud_score(applicant_id: int):
    await asyncio.sleep(1.5)
    return {"fraud_probability": round(random.random(), 2)}


async def fetch_macro_risk():
    await asyncio.sleep(1.9)
    return {"macro_risk_index": round(random.uniform(0.1, 1.0), 2)}
