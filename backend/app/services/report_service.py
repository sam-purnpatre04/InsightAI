from datetime import datetime


def generate_report(
    filename,
    dataset_profile,
    cleaning_summary,
    eda,
    business_insights
):
    """
    Generates a professional dataset report.
    """

    report = {
        "report_metadata": {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dataset_name": filename
        },

        "dataset_overview": {
            "rows": dataset_profile["rows"],
            "columns": dataset_profile["columns"],
            "memory_usage_kb": dataset_profile["memory_usage_kb"]
        },

        "data_quality": {
            "duplicate_rows": dataset_profile["duplicate_rows"],
            "missing_values": dataset_profile["missing_values"],
            "duplicates_removed": cleaning_summary["duplicates_removed"],
            "cleaned_rows": cleaning_summary["cleaned_rows"]
        },

        "column_information": {
            "numerical_columns": dataset_profile["numerical_columns"],
            "categorical_columns": dataset_profile["categorical_columns"],
            "datetime_columns": dataset_profile["datetime_columns"],
            "boolean_columns": dataset_profile["boolean_columns"]
        },

        "statistical_summary": eda["numerical_summary"],

        "categorical_summary": eda["categorical_summary"],

        "correlation_matrix": eda["correlation_matrix"],

        "business_insights": business_insights,

        "report_summary": create_summary(
            dataset_profile,
            cleaning_summary,
            business_insights
        )
    }

    return report


def create_summary(
    dataset_profile,
    cleaning_summary,
    business_insights
):
    """
    Generates an executive summary.
    """

    summary = []

    summary.append(
        f"The uploaded dataset contains {dataset_profile['rows']} rows "
        f"and {dataset_profile['columns']} columns."
    )

    total_missing = sum(
        dataset_profile["missing_values"].values()
    )

    summary.append(
        f"Total missing values detected: {total_missing}."
    )

    summary.append(
        f"Duplicate rows detected: "
        f"{dataset_profile['duplicate_rows']}."
    )

    summary.append(
        f"Duplicates removed during cleaning: "
        f"{cleaning_summary['duplicates_removed']}."
    )

    summary.append(
        f"Final cleaned dataset contains "
        f"{cleaning_summary['cleaned_rows']} rows."
    )

    summary.append(
        f"Numerical Features: "
        f"{len(dataset_profile['numerical_columns'])}"
    )

    summary.append(
        f"Categorical Features: "
        f"{len(dataset_profile['categorical_columns'])}"
    )

    summary.append(
        "Business insights have been generated automatically "
        "using the statistical analysis engine."
    )

    if len(business_insights) > 0:
        summary.append(
            f"Total AI-generated insights: "
            f"{len(business_insights)}."
        )

    return summary