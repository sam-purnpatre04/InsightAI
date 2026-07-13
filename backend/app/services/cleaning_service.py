import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names by removing extra spaces,
    converting to lowercase, and replacing spaces with underscores.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def remove_duplicates(df: pd.DataFrame):
    """
    Remove duplicate rows from the dataset.
    """

    duplicates_removed = int(df.duplicated().sum())

    df = df.drop_duplicates()

    return df, duplicates_removed


def handle_missing_values(df: pd.DataFrame):
    """
    Fill missing values.

    Numerical columns -> Median
    Categorical columns -> Mode
    """

    missing_before = df.isnull().sum().to_dict()

    numerical_columns = df.select_dtypes(include=["number"]).columns

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in numerical_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].median())

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode = df[column].mode()

            if not mode.empty:
                df[column] = df[column].fillna(mode[0])

    missing_after = df.isnull().sum().to_dict()

    return df, missing_before, missing_after


def detect_outliers(df: pd.DataFrame):
    """
    Detect outliers using the IQR method.
    """

    outlier_summary = {}

    numerical_columns = df.select_dtypes(include=["number"]).columns

    for column in numerical_columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[
            (df[column] < lower) |
            (df[column] > upper)
        ]

        outlier_summary[column] = len(outliers)

    return outlier_summary


def clean_dataset(df: pd.DataFrame):
    """
    Complete data cleaning pipeline.
    """

    original_rows = len(df)

    df = standardize_column_names(df)

    df, duplicates_removed = remove_duplicates(df)

    df, missing_before, missing_after = handle_missing_values(df)

    outliers = detect_outliers(df)

    cleaned_rows = len(df)

    summary = {
        "original_rows": original_rows,
        "cleaned_rows": cleaned_rows,
        "duplicates_removed": duplicates_removed,
        "missing_values_before": missing_before,
        "missing_values_after": missing_after,
        "outliers_detected": outliers
    }

    return df, summary