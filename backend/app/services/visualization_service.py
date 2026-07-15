import os
import matplotlib.pyplot as plt
import pandas as pd


REPORT_FOLDER = "reports"


def generate_visualizations(df: pd.DataFrame):
    """
    Generate basic charts for all numerical columns.
    Saves images into the reports folder.
    """

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    generated_files = []

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:

        plt.figure(figsize=(6, 4))

        df[column].hist(bins=20)

        plt.title(column)

        plt.xlabel(column)

        plt.ylabel("Frequency")

        filename = f"{column}_histogram.png"

        filepath = os.path.join(REPORT_FOLDER, filename)

        plt.tight_layout()

        plt.savefig(filepath)

        plt.close()

        generated_files.append(filename)

    return generated_files