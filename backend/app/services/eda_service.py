import pandas as pd


def generate_eda(df: pd.DataFrame):
    """
    Generate Exploratory Data Analysis (EDA)
    for the uploaded dataset.
    """

    # -----------------------------
    # Numerical Summary
    # -----------------------------
    numerical_summary = (
        df.describe()
        .round(2)
        .fillna("")
        .to_dict()
    )

    # -----------------------------
    # Categorical Summary
    # -----------------------------
    categorical_summary = {}

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        categorical_summary[column] = {
            "unique_values": int(df[column].nunique()),
            "most_frequent": (
                df[column].mode().iloc[0]
                if not df[column].mode().empty
                else None
            ),
            "top_5_values": (
                df[column]
                .value_counts()
                .head(5)
                .to_dict()
            )
        }

    # -----------------------------
    # Correlation Matrix
    # -----------------------------
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.shape[1] >= 2:
        correlation_matrix = (
            numeric_df
            .corr()
            .round(2)
            .fillna("")
            .to_dict()
        )
    else:
        correlation_matrix = {}

    # -----------------------------
    # Return EDA
    # -----------------------------
    return {
        "numerical_summary": numerical_summary,
        "categorical_summary": categorical_summary,
        "correlation_matrix": correlation_matrix
    }