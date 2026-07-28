import pandas as pd


def generate_eda(df: pd.DataFrame):
    """
    Generate Exploratory Data Analysis (EDA)
    including numerical statistics, categorical
    statistics, correlations, and outlier detection.
    """

    # =====================================================
    # NUMERICAL SUMMARY
    # =====================================================

    numerical_summary = (
        df.describe()
        .round(2)
        .fillna("")
        .to_dict()
    )

    # =====================================================
    # CATEGORICAL SUMMARY
    # =====================================================

    categorical_summary = {}

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        mode = df[column].mode()

        categorical_summary[column] = {

            "unique_values": int(
                df[column].nunique()
            ),

            "most_frequent": (
                mode.iloc[0]
                if not mode.empty
                else None
            ),

            "top_5_values": (
                df[column]
                .value_counts()
                .head(5)
                .to_dict()
            )
        }

    # =====================================================
    # CORRELATION MATRIX
    # =====================================================

    numeric_df = df.select_dtypes(
        include=["number"]
    )

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

    # =====================================================
    # OUTLIER DETECTION
    # =====================================================

    outlier_summary = {}

    for column in numeric_df.columns:

        # Remove missing values
        series = numeric_df[column].dropna()

        # Need enough data to calculate meaningful quartiles
        if len(series) < 4:
            continue

        # Calculate quartiles
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)

        # Calculate IQR
        iqr = q3 - q1

        # Calculate boundaries
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        # Identify outliers
        outliers = series[
            (series < lower_bound) |
            (series > upper_bound)
        ]

        outlier_count = len(outliers)

        total_values = len(series)

        outlier_percentage = (
            outlier_count / total_values * 100
            if total_values > 0
            else 0
        )

        outlier_summary[column] = {

            "outlier_count": int(
                outlier_count
            ),

            "outlier_percentage": round(
                outlier_percentage,
                2
            ),

            "q1": round(
                float(q1),
                2
            ),

            "q3": round(
                float(q3),
                2
            ),

            "iqr": round(
                float(iqr),
                2
            ),

            "lower_bound": round(
                float(lower_bound),
                2
            ),

            "upper_bound": round(
                float(upper_bound),
                2
            )
        }

    # =====================================================
    # RETURN EDA
    # =====================================================

    return {

        "numerical_summary":
            numerical_summary,

        "categorical_summary":
            categorical_summary,

        "correlation_matrix":
            correlation_matrix,

        "outlier_summary":
            outlier_summary
    }