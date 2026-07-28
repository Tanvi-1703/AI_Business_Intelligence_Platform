import os
import pandas as pd

from config import UPLOAD_FOLDER, SUPPORTED_FILES


def load_dataset(filename):

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(filepath):
        print("\nFile not found.")
        return None

    extension = os.path.splitext(filename)[1].lower()

    if extension not in SUPPORTED_FILES:
        print("\nUnsupported file.")
        return None

    try:

        if extension == ".csv":
            df = pd.read_csv(filepath)

        elif extension == ".xlsx":
            df = pd.read_excel(filepath)

        else:
            return None

        return df

    except Exception as e:

        print(e)

        return None


def dataset_summary(df):

    print("\n========== DATASET SUMMARY ==========\n")

    print("Rows :", df.shape[0])

    print("Columns :", df.shape[1])

    print("\nColumn Names")

    print(df.columns.tolist())

    print("\nData Types")

    print(df.dtypes)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nPreview")

    print(df.head())