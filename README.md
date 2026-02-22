# python-foundation
First Python project to understand the syntax and running application

# Weather Report:
Created small application which takes coordinates and dates and fetch the weather for this particular timeframe, plots on graphs and save both graph and csv file to data folder

# Data Processing Module

Purpose:
This module ingests raw applicant data, cleans it, performs feature engineering, and prepares the dataset for ML risk modeling.

Features:
- Data loading
- Missing value handling
- Data validation
- Feature engineering
- Logging
- Reusable pipeline class

# main_async
A service that asynchronously calls multiple external AI service (simulated) to enrich loan risk data.
run : python main_async.py

# Loan Risk Inference API (AI Microservice)
Designed and deployed an asynchronous AI inference microservice using FastAPI with schema validation and dependency injection.

Run : python -m uvicorn src.api.main:app --reload
Open : http://127.0.0.1:8000/docs
Will get Swagger UI automatically.