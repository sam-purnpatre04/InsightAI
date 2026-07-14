import pandas as pd
from backend.app.services.profiling_service import get_dataset_profile
from backend.app.services.cleaning_service import clean_dataset


def read_csv(upload_file):
    """
    Reads an uploaded CSV file, profiles it,
    cleans it, and returns a complete summary.
    """

    # Read CSV
    df = pd.read_csv(upload_file.file)

    # ----------------------------
    dataset_profile = get_dataset_profile(df)

    missing_values = df.isnull().sum().to_dict()

    duplicate_rows = int(df.duplicated().sum())

    memory_usage = round(df.memory_usage(deep=True).sum() / 1024, 2)

    numerical_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # ----------------------------
    # Data Cleaning
    # ----------------------------

    cleaned_df, cleaning_summary = clean_dataset(df)

    # ----------------------------
    # Return Response
    # ----------------------------

    return {

        "filename": upload_file.filename,

       "dataset_profile": dataset_profile,
        "cleaning_summary": cleaning_summary

    }
