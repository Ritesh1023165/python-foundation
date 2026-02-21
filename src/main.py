import requests
import numpy as np
from data_processing import LoanDataProcessor
from config import OUTPUT_DATA_DIR

# print("Hello world !!!")
# response = requests.get("https://api.github.com")
# print(response.status_code)

if __name__ == "__main__":
    processor = LoanDataProcessor("loan_data.csv")
    processed_df = processor.process()
    print(processed_df.head())
    # Save to CSV
    processed_df.to_csv(OUTPUT_DATA_DIR/'Loan_data_processed.csv', index=False)
    print("Data saved to data/Loan_data_processed.csv")