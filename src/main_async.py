import asyncio
from risk_enricher import enrich_applicant


async def main():
    applicant_id = 1001
    result = await enrich_applicant(applicant_id)
    print("Enriched Risk Profile:")
    print(result)


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        print("No Event Loop running")
        loop = None
    print("Starting main")
    if loop and loop.is_running():
        print("Running inside existing loop ")
        task = loop.create_task(main())
    else:
        asyncio.run(main())
    print("main complete")