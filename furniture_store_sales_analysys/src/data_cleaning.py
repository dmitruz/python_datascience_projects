"""
data_cleaning.py
-----------------
Loads the raw GA-style session-level dataset for the furniture store,
cleans it, and engineers the fields used throughout the analysis.

Usage:
    python src/data_cleaning.py
        --input data/raw/final_dataset.csv
        --output data/processed/cleaned_sessions.csv
"""

import argparse
import pandas as pd
import numpy as np


def load_raw_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # --- Types ---
    df["order_date"] = pd.to_datetime(df["order_date"])

    # --- Missing value handling ---
    # A session with no product_name never converted to a sale.
    df["browser_language"] = df["browser_language"].fillna("unknown")
    df["country"] = df["country"].replace("(not set)", "unknown")

    # --- Feature engineering ---
    # A session is a "purchase" if it has an associated product.
    df["purchased"] = df["product_name"].notna()

    # A session belongs to a signed-in user if registered_user_id is populated.
    df["is_registered"] = df["registered_user_id"].notna()

    # is_subscribed / email_verified as clean booleans
    df["is_subscribed"] = df["is_subscribed"].astype(bool)
    df["email_verified"] = df["email_verified"].fillna(0).astype(bool)

    # Calendar helpers used throughout the EDA
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    df["order_weekday"] = df["order_date"].dt.day_name()

    # Revenue is only meaningful for converted sessions.
    df["revenue"] = np.where(df["purchased"], df["price"], 0.0)

    # Drop obvious duplicate sessions if any exist.
    df = df.drop_duplicates(subset=["ga_session_id"])

    return df


def main():
    parser = argparse.ArgumentParser(description="Clean the furniture store session dataset.")
    parser.add_argument("--input", default="data/raw/final_dataset.csv")
    parser.add_argument("--output", default="data/processed/cleaned_sessions.csv")
    args = parser.parse_args()

    print(f"Loading raw data from {args.input} ...")
    raw = load_raw_data(args.input)
    print(f"Raw shape: {raw.shape}")

    print("Cleaning and engineering features ...")
    cleaned = clean_data(raw)
    print(f"Cleaned shape: {cleaned.shape}")

    cleaned.to_csv(args.output, index=False)
    print(f"Saved cleaned dataset to {args.output}")


if __name__ == "__main__":
    main()
