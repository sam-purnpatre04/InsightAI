import pandas as pd


def get_dataset_profile(df: pd.DataFrame):
    """
    Generate a complete profile of the uploaded dataset.
    """

    # Basic Information
    rows = df.shape[0]
    columns = df.shape[1]

    # Column Names
    column_names = df.columns.tolist()

    # Data Types
    data_types = {
        column: str(dtype)
        for column, dtype in df.dtypes.items()
    }

    # Missing Values
    missing_values = df.isnull().sum().to_dict()

    # Duplicate Rows
    duplicate_rows = int(df.duplicated().sum())

    # Memory Usage (KB)
    memory_usage = round(
        df.memory_usage(deep=True).sum() / 1024,
        2
    )

    # Numerical Columns
    numerical_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    # Categorical Columns
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # Datetime Columns
    datetime_columns = df.select_dtypes(
        include=["datetime", "datetimetz"]
    ).columns.tolist()

    # Boolean Columns
    boolean_columns = df.select_dtypes(
        include=["bool"]
    ).columns.tolist()

    profile = {
        "rows": rows,
        "columns": columns,
        "column_names": column_names,
        "data_types": data_types,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "memory_usage_kb": memory_usage,
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,
        "datetime_columns": datetime_columns,
        "boolean_columns": boolean_columns
    }

    return profile