import os
import pandas as pd

from config import CLEAN_FOLDER


def clean_dataset(df):

    print("\nCleaning Dataset...")

    original_rows = len(df)

    # -----------------------
    # Remove duplicate rows
    # -----------------------

    df = df.drop_duplicates()

    duplicate_rows = original_rows - len(df)

    # -----------------------
    # Standardize column names
    # -----------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # -----------------------
    # Remove spaces from text columns
    # -----------------------

    for column in df.select_dtypes(include="object").columns:

        df[column] = df[column].astype(str).str.strip()

    # -----------------------
    # Fill missing numeric values
    # -----------------------

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        df[column] = df[column].fillna(df[column].mean())

    # -----------------------
    # Fill missing text values
    # -----------------------

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:

        df[column] = df[column].fillna("Unknown")

    print("Duplicate Rows Removed :", duplicate_rows)

    print("Cleaning Completed Successfully.")

    return df


def save_clean_dataset(df):

    filepath = os.path.join(CLEAN_FOLDER, "cleaned_sales.csv")

    df.to_csv(filepath, index=False)

    print("\nClean Dataset Saved")

    print(filepath)