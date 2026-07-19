import pandas as pd

from backend.app.services.profiling_service import get_dataset_profile
from backend.app.services.cleaning_service import clean_dataset
from backend.app.services.eda_service import generate_eda
from backend.app.services.insights_service import generate_insights
from backend.app.services.visualization_service import generate_visualizations
from backend.app.services.report_service import generate_report


def read_csv(upload_file):
    """
    Reads uploaded CSV files with automatic encoding detection,
    performs profiling, cleaning, EDA, visualization,
    business insight generation and report generation.
    """

    # -----------------------------
    # Read CSV with multiple encodings
    # -----------------------------

    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp1252",
        "latin1",
        "ISO-8859-1",
    ]

    df = None

    last_error = None

    for encoding in encodings:

        try:

            upload_file.file.seek(0)

            df = pd.read_csv(
                upload_file.file,
                encoding=encoding,
                low_memory=False
            )

            print(f"CSV loaded successfully using {encoding}")

            break

        except UnicodeDecodeError as e:

            last_error = e

        except Exception as e:

            last_error = e

    if df is None:

        raise Exception(
            f"Unable to read uploaded CSV.\n{last_error}"
        )

    # -----------------------------
    # Dataset Profile
    # -----------------------------

    dataset_profile = get_dataset_profile(df)

    # -----------------------------
    # Cleaning
    # -----------------------------

    cleaned_df, cleaning_summary = clean_dataset(df)

    # -----------------------------
    # EDA
    # -----------------------------

    eda = generate_eda(cleaned_df)

    # -----------------------------
    # Charts
    # -----------------------------

    charts = generate_visualizations(cleaned_df)

    # -----------------------------
    # AI Insights
    # -----------------------------

    insights = generate_insights(
        cleaned_df,
        dataset_profile,
        cleaning_summary,
        eda
    )

    # -----------------------------
    # Final Report
    # -----------------------------

    report = generate_report(
        upload_file.filename,
        dataset_profile,
        cleaning_summary,
        eda,
        insights
    )

    # -----------------------------
    # Response
    # -----------------------------

    return {

        "filename": upload_file.filename,

        "dataset_profile": dataset_profile,

        "cleaning_summary": cleaning_summary,

        "eda": eda,

        "business_insights": insights,

        "generated_charts": charts,

        "report": report

    }