import os
import warnings

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

# ======================================================
# CONFIGURATION
# ======================================================

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

sns.set_theme(style="whitegrid")

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 120
plt.rcParams["savefig.dpi"] = 120
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12


# ======================================================
# SAVE CHART
# ======================================================

def save_chart(filename):

    filepath = os.path.join(REPORT_FOLDER, filename)

    plt.tight_layout()

    plt.savefig(filepath, bbox_inches="tight")

    plt.close()

    return filename


# ======================================================
# COLUMN HELPERS
# ======================================================

def get_numeric_columns(df):

    return df.select_dtypes(include=np.number).columns.tolist()


def get_categorical_columns(df):

    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


# ======================================================
# DATE DETECTION
# ======================================================

def detect_datetime_column(df):

    for column in df.columns:

        try:

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            if converted.notna().sum() > len(df) * 0.70:

                df[column] = converted

                return column

        except:

            pass

    return None


# ======================================================
# HISTOGRAM
# ======================================================

def histogram(df, column):

    plt.figure()

    sns.histplot(
        df[column].dropna(),
        kde=True,
        color="steelblue"
    )

    plt.title(f"{column} Distribution")

    plt.xlabel(column)

    plt.ylabel("Frequency")

    return save_chart(
        f"{column}_histogram.png"
    )


# ======================================================
# BOXPLOT
# ======================================================

def boxplot(df, column):

    plt.figure()

    sns.boxplot(
        x=df[column],
        color="orange"
    )

    plt.title(f"{column} Box Plot")

    return save_chart(
        f"{column}_boxplot.png"
    )


# ======================================================
# MISSING VALUES CHART
# ======================================================

def missing_values_chart(df):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:

        return None

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=missing.index,
        y=missing.values
    )

    plt.xticks(rotation=45)

    plt.title("Missing Values")

    plt.ylabel("Missing Count")

    return save_chart(
        "missing_values.png"
    )


# ======================================================
# MAIN FUNCTION
# ======================================================

def generate_visualizations(df: pd.DataFrame):

    generated_files = []

    numeric_columns = get_numeric_columns(df)

    # Histograms + Boxplots

    for column in numeric_columns:

        try:

            generated_files.append(
                histogram(df, column)
            )

        except Exception as e:

            print(
                f"Histogram Error ({column}): {e}"
            )

        try:

            generated_files.append(
                boxplot(df, column)
            )

        except Exception as e:

            print(
                f"Boxplot Error ({column}): {e}"
            )

    # Missing Values

    try:

        missing = missing_values_chart(df)

        if missing:

            generated_files.append(missing)

    except Exception as e:

        print(e)

    return generated_files