import pandas as pd

from backend.app.services.cleaning_service import clean_dataset


def read_csv(upload_file):
    """
    Reads an uploaded CSV file, profiles it,
    cleans it, and returns a complete summary.
    """

    # Read CSV
    df = pd.read_csv(upload_file.file)

    # ----------------------------
    # Dataset Profile
    # ----------------------------

    rows = df.shape[0]
    columns = df.shape[1]

    column_names = df.columns.tolist()

    data_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

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

        "dataset_profile": {
            "rows": rows,
            "columns": columns,
            "column_names": column_names,
            "data_types": data_types,
            "missing_values": missing_values,
            "duplicate_rows": duplicate_rows,
            "memory_usage_kb": memory_usage,
            "numerical_columns": numerical_columns,
            "categorical_columns": categorical_columns
        },

        "cleaning_summary": cleaning_summary

    }
