import pandas as pd
import numpy as np
import logging
from config import INPUT_DATA_DIR
from config import OUTPUT_DATA_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoanDataProcessor:

    def __init__(self, file_path: str):
        self.file_path = INPUT_DATA_DIR/file_path
        # dataframe
        self.df = None
        logger.info(f"Input Flie_path: {self.file_path}")
    
    # -----------------------------
    # Load Data
    # -----------------------------
    def load_data(self):
        logger.info("Loading dataset...")
        self.df = pd.read_csv(self.file_path)
        logger.info(f"Dataset loaded with {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        return self.df

    # -----------------------------
    # Clean Data
    # -----------------------------
    def clean_data(self):
        logger.info("Cleaning dataset...")
        # Fill missing income with median
        if self.df["income"].isnull().sum() > 0:
            median_income = self.df["income"].median()
            self.df.fillna({"income": median_income}, inplace=True)
            logger.info(f"Filled missing income with median value {median_income}")
        
        # Drop rows with missing credit score
        self.df = self.df.dropna(subset=["credit_score"])
        
        # Remove negative loan amounts
        self.df = self.df[self.df["loan_amount"] > 0]

        # Standardize city names
        self.df["city"] = self.df["city"].str.lower().str.title()
        
        logger.info("Data cleaning complete")
        return self.df

    # -----------------------------
    # Feature Engineering
    # -----------------------------
    def engineer_features(self):
        logger.info("Creating engineered features...")

        # Loan to income ratio
        self.df["loan_income_ratio"] = (
            self.df["loan_amount"] / self.df["income"]
        )

        # Risk flag based on credit score
        def risk_category(score):
            if score < 600:
                return "high"
            elif score < 700:
                return "medium"
            return "low"

        self.df["risk_flag"] = self.df["credit_score"].apply(risk_category)

        # Employment stability score (log transform)
        self.df["employment_score"] = np.log1p(self.df["employment_years"])

        logger.info("Feature engineering complete")
        return self.df

    # -----------------------------
    # Validate Data
    # -----------------------------
    def validate_data(self):
        logger.info("Validating dataset...")

        if (self.df["age"] < 18).any():
            raise ValueError("Invalid age detected (<18)")

        if (self.df["income"] <= 0).any():
            raise ValueError("Invalid income detected (<=0)")

        logger.info("Validation successful")


    # -----------------------------
    # Full Pipeline
    # -----------------------------
    def process(self):
        self.load_data()
        self.clean_data()
        self.engineer_features()
        self.validate_data()
        logger.info("Data processing pipeline completed successfully")
        return self.df



if __name__ == "__main__":
    logger.info("Testing the class")
    processor = LoanDataProcessor("loan_data.csv")
    processed_df = processor.process()
    print(processed_df.head())
    # Save to CSV
    processed_df.to_csv(OUTPUT_DATA_DIR/'Loan_data_processed.csv', index=False)
    logger.info("Data saved to data/Loan_data_processed.csv")

    
