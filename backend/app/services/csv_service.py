import pandas as pd

from backend.app.services.profiling_service import get_dataset_profile
from backend.app.services.cleaning_service import clean_dataset
from backend.app.services.eda_service import generate_eda
from backend.app.services.insights_service import generate_insights
from backend.app.services.visualization_service import generate_visualizations
from backend.app.services.report_service import generate_report


encodings = [
    "utf-8",
    "utf-8-sig",
    "cp1252",
    "latin1",
    "ISO-8859-1",
]

df = None

for encoding in encodings:
    try:
        upload_file.file.seek(0)
        df = pd.read_csv(upload_file.file, encoding=encoding)
        print(f"Loaded using encoding: {encoding}")
        break
    except UnicodeDecodeError:
        continue

if df is None:
    raise Exception("Unable to read CSV. Unsupported file encoding.")
    """
    Reads an uploaded CSV file,
    profiles it,
    cleans it,
    performs EDA,
    generates charts,
    and returns business insights.
    """

    # Read CSV
    df = pd.read_csv(upload_file.file)

    # Dataset Profile
    dataset_profile = get_dataset_profile(df)

    # Clean Dataset
    cleaned_df, cleaning_summary = clean_dataset(df)

    # Exploratory Data Analysis
    eda = generate_eda(cleaned_df)

    # Generate Charts
    charts = generate_visualizations(cleaned_df)

    # Business Insights
    insights = generate_insights(
        cleaned_df,
        dataset_profile,
        cleaning_summary,
        eda
    )
    report = generate_report(
    upload_file.filename,
    dataset_profile,
    cleaning_summary,
    eda,
    insights
)

    # Return Response
    return {
    "filename": upload_file.filename,
    "dataset_profile": dataset_profile,
    "cleaning_summary": cleaning_summary,
    "eda": eda,
    "business_insights": insights,
    "generated_charts": charts,
    "report": report
}