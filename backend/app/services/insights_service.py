import pandas as pd


def generate_insights(
    df: pd.DataFrame,
    dataset_profile: dict,
    cleaning_summary: dict,
    eda: dict
):
    """
    Generate business-friendly insights from
    the dataset profile, cleaning summary,
    and EDA results.
    """

    insights = []

    # -----------------------------
    # Dataset Overview
    # -----------------------------
    insights.append(
        f"The dataset contains {dataset_profile['rows']} rows and {dataset_profile['columns']} columns."
    )

    # -----------------------------
    # Missing Values
    # -----------------------------
    total_missing = sum(
        dataset_profile["missing_values"].values()
    )

    if total_missing == 0:
        insights.append(
            "No missing values were found in the uploaded dataset."
        )
    else:
        insights.append(
            f"The dataset contained {total_missing} missing values before cleaning."
        )

    # -----------------------------
    # Duplicate Rows
    # -----------------------------
    duplicates = cleaning_summary["duplicates_removed"]

    if duplicates == 0:
        insights.append(
            "No duplicate rows were detected."
        )
    else:
        insights.append(
            f"{duplicates} duplicate rows were removed."
        )

    # -----------------------------
    # Numerical Insights
    # -----------------------------
    numerical_summary = eda["numerical_summary"]

    for column, stats in numerical_summary.items():

        insights.append(
            f"The average {column} is {stats['mean']}."
        )

        insights.append(
            f"{column} ranges from {stats['min']} to {stats['max']}."
        )

    # -----------------------------
    # Categorical Insights
    # -----------------------------
    categorical_summary = eda["categorical_summary"]

    for column, stats in categorical_summary.items():

        insights.append(
            f"{column} contains {stats['unique_values']} unique values."
        )

        insights.append(
            f"The most common {column} is '{stats['most_frequent']}'."
        )

    # -----------------------------
    # Correlation Insights
    # -----------------------------
    correlation_matrix = eda["correlation_matrix"]

    checked = set()

    for col1 in correlation_matrix:

        for col2 in correlation_matrix[col1]:

            if col1 == col2:
                continue

            pair = tuple(sorted((col1, col2)))

            if pair in checked:
                continue

            checked.add(pair)

            value = correlation_matrix[col1][col2]

            if abs(value) >= 0.70:

                insights.append(
                    f"There is a strong correlation ({value}) between {col1} and {col2}."
                )

            elif abs(value) >= 0.50:

                insights.append(
                    f"There is a moderate correlation ({value}) between {col1} and {col2}."
                )

    return insights