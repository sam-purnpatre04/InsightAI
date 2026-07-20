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

        if pd.api.types.is_datetime64_any_dtype(df[column]):
            return column

        try:

            converted = pd.to_datetime(
                df[column],
                errors="coerce",
                infer_datetime_format=True
            )

            if converted.notna().mean() >= 0.7:
                df[column] = converted
                return column

        except Exception:
            continue

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
# SCATTER PLOT
# ======================================================

def scatter_plot(df, numeric_columns):

    if len(numeric_columns) < 2:
        return None

    x = numeric_columns[0]
    y = numeric_columns[1]

    temp = df[[x, y]].dropna()

    if temp.empty:
        return None

    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=temp,
        x=x,
        y=y,
        color="royalblue"
    )

    plt.title(f"{x} vs {y}")

    return save_chart(f"{x}_vs_{y}_scatter.png")

# ======================================================
# CORRELATION HEATMAP
# ======================================================

def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.shape[1] < 2:
        return None

    corr = numeric_df.corr(numeric_only=True)

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        square=True
    )

    plt.title("Correlation Heatmap")

    return save_chart("correlation_heatmap.png")

# ======================================================
# LINE CHART
# ======================================================

def line_chart(df):

    date_column = detect_datetime_column(df)

    if date_column is None:
        return None

    numeric_columns = get_numeric_columns(df)

    if not numeric_columns:
        return None

    value_column = numeric_columns[0]

    temp = (
        df[[date_column, value_column]]
        .dropna()
        .sort_values(date_column)
    )

    if temp.empty:
        return None

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=temp,
        x=date_column,
        y=value_column,
        marker="o",
        color="green"
    )

    plt.title(f"{value_column} Trend Over Time")

    plt.xlabel(date_column)

    plt.ylabel(value_column)

    plt.xticks(rotation=45)

    return save_chart(f"{value_column}_trend.png")

# ======================================================
# BAR CHART
# ======================================================

def bar_chart(df, column):

    value_counts = (
        df[column]
        .fillna("Missing")
        .value_counts()
        .head(10)
    )

    if value_counts.empty:
        return None

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=value_counts.index,
        y=value_counts.values,
        palette="viridis"
    )

    plt.title(f"{column} Distribution")

    plt.xlabel(column)

    plt.ylabel("Count")

    plt.xticks(rotation=45)

    return save_chart(f"{column}_bar_chart.png")


# ======================================================
# PIE CHART
# ======================================================

def pie_chart(df, column):

    value_counts = (
        df[column]
        .fillna("Missing")
        .value_counts()
        .head(8)
    )

    if value_counts.empty:
        return None

    plt.figure(figsize=(7, 7))

    plt.pie(
        value_counts.values,
        labels=value_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(f"{column} Distribution")

    plt.axis("equal")

    return save_chart(f"{column}_pie_chart.png")

# ======================================================
# MAIN FUNCTION
# ======================================================

def generate_visualizations(df: pd.DataFrame):

    generated_files = []

    numeric_columns = get_numeric_columns(df)

    # ------------------------------------------
    # Histogram & Boxplot
    # ------------------------------------------

    for column in numeric_columns:

        try:
            chart = histogram(df, column)
            if chart:
                generated_files.append(chart)
        except Exception as e:
            print(f"Histogram Error ({column}): {e}")

        try:
            chart = boxplot(df, column)
            if chart:
                generated_files.append(chart)
        except Exception as e:
            print(f"Boxplot Error ({column}): {e}")

    # ------------------------------------------
    # Scatter Plot
    # ------------------------------------------

    try:
        chart = scatter_plot(df, numeric_columns)

        if chart:
            generated_files.append(chart)

    except Exception as e:
        print(f"Scatter Error: {e}")

    # ------------------------------------------
    # Correlation Heatmap
    # ------------------------------------------

    try:
        chart = correlation_heatmap(df)

        if chart:
            generated_files.append(chart)

    except Exception as e:
        print(f"Heatmap Error: {e}")

    # ------------------------------------------
    # Line Chart
    # ------------------------------------------

    try:
        chart = line_chart(df)

        if chart:
            generated_files.append(chart)

    except Exception as e:
        print(f"Line Chart Error: {e}")

    # ------------------------------------------
    # Missing Values Chart
    # ------------------------------------------

    try:
        chart = missing_values_chart(df)

        if chart:
            generated_files.append(chart)

    except Exception as e:
        print(f"Missing Values Chart Error: {e}")

    # ------------------------------------------
    # Bar Charts & Pie Charts
    # ------------------------------------------

    categorical_columns = get_categorical_columns(df)

    for column in categorical_columns:

        try:
            chart = bar_chart(df, column)

            if chart:
                generated_files.append(chart)

        except Exception as e:
            print(f"Bar Chart Error ({column}): {e}")

        try:
            chart = pie_chart(df, column)

            if chart:
                generated_files.append(chart)

        except Exception as e:
            print(f"Pie Chart Error ({column}): {e}")

    return generated_files