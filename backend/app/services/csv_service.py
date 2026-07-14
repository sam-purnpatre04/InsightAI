import pandas as pd
from backend.app.services.eda_service import generate_eda
from backend.app.services.profiling_service import get_dataset_profile
from backend.app.services.cleaning_service import clean_dataset


def read_csv(upload_file):
    """
    Reads an uploaded CSV file, profiles it,
    cleans it, and returns a complete summary.
    """

    # Read CSV
    df = pd.read_csv(upload_file.file)

    # Dataset Profile
    dataset_profile = get_dataset_profile(df)

    # Clean Dataset
    cleaned_df, cleaning_summary = clean_dataset(df)

    # Exploratory Data Analysis
    eda = generate_eda(cleaned_df)

    # Return Response
    return {
        "filename": upload_file.filename,
        "dataset_profile": dataset_profile,
        "cleaning_summary": cleaning_summary,
        "eda": eda
    }