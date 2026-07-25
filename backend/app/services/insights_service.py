import pandas as pd
import numpy as np


# =====================================================
# COLUMN DETECTION
# =====================================================

def find_column(df, keywords):
    """
    Finds the first column whose name contains
    one of the given keywords.
    """

    for column in df.columns:

        name = column.lower()

        for keyword in keywords:

            if keyword in name:
                return column

    return None


# =====================================================
# DATA QUALITY SCORE
# =====================================================

def calculate_data_quality(df, cleaning_summary):

    total_cells = df.shape[0] * df.shape[1]

    missing = df.isnull().sum().sum()

    duplicate_rows = cleaning_summary["duplicates_removed"]

    missing_percent = (
        missing / total_cells * 100
        if total_cells > 0
        else 0
    )

    duplicate_percent = (
        duplicate_rows / len(df) * 100
        if len(df) > 0
        else 0
    )

    score = 100

    score -= missing_percent * 0.6

    score -= duplicate_percent * 0.4

    score = max(0, min(100, round(score, 1)))

    return score


# =====================================================
# DATASET SUMMARY
# =====================================================

def generate_dataset_summary(
    df,
    dataset_profile,
    cleaning_summary,
    insights
):

    rows = dataset_profile["rows"]

    columns = dataset_profile["columns"]

    memory = dataset_profile["memory_usage_kb"]

    quality = calculate_data_quality(
        df,
        cleaning_summary
    )

    insights.append({
        "type": "summary",
        "title": "Dataset Overview",
        "description":
            f"The uploaded dataset contains {rows:,} rows "
            f"and {columns} columns."
    })

    insights.append({
        "type": "summary",
        "title": "Memory Usage",
        "description":
            f"The dataset occupies approximately "
            f"{memory:,.2f} KB in memory."
    })

    insights.append({
        "type": "summary",
        "title": "Data Quality Score",
        "description":
            f"Overall data quality score is "
            f"{quality}/100."
    })


# =====================================================
# =====================================================
# MISSING VALUE INSIGHTS
# =====================================================

def generate_missing_value_insights(
    dataset_profile,
    insights
):

    missing = dataset_profile["missing_values"]

    total_missing = sum(missing.values())

    # No missing values
    if total_missing == 0:

        insights.append({

            "type": "success",

            "title": "Missing Values",

            "description":
                "No missing values were detected."

        })

        return

    # Missing values found
    for column, value in missing.items():

        if value > 0:

            percent = (
                value / dataset_profile["rows"]
            ) * 100

            if percent >= 30:
                level = "warning"

            elif percent >= 10:
                level = "info"

            else:
                level = "summary"

            insights.append({

                "type": level,

                "title": f"Missing Values - {column}",

                "description":
                    f"{value:,} missing values "
                    f"({percent:.1f}%) were detected before cleaning."

            })
        return

    for column, value in total_missing.items():

        percent = (
            value / len(df)
        ) * 100

        if percent >= 30:

            level = "warning"

        elif percent >= 10:

            level = "info"

        else:

            level = "summary"

        insights.append({

            "type": level,

            "title": f"Missing Values - {column}",

            "description":
                f"{value:,} values "
                f"({percent:.1f}%) are missing."
        })


# =====================================================
# DUPLICATE INSIGHTS
# =====================================================

def generate_duplicate_insights(
    cleaning_summary,
    insights
):

    duplicates = cleaning_summary[
        "duplicates_removed"
    ]

    if duplicates == 0:

        insights.append({

            "type": "success",

            "title": "Duplicate Rows",

            "description":
                "No duplicate rows were found."
        })

    else:

        insights.append({

            "type": "warning",

            "title": "Duplicate Rows",

            "description":
                f"{duplicates:,} duplicate rows "
                f"were removed."
        })
# =====================================================
# SALES INSIGHTS
# =====================================================

def generate_sales_insights(df, insights):

    sales_column = find_column(
        df,
        ["sales", "revenue", "amount"]
    )

    if sales_column is None:
        return

    total_sales = df[sales_column].sum()

    average_sales = df[sales_column].mean()

    highest_sale = df[sales_column].max()

    insights.append({

        "type": "summary",

        "title": "Total Sales",

        "description":
            f"Total sales amount is ₹{total_sales:,.2f}."

    })

    insights.append({

        "type": "summary",

        "title": "Average Sales",

        "description":
            f"Average transaction value is ₹{average_sales:,.2f}."

    })

    insights.append({

        "type": "info",

        "title": "Highest Sale",

        "description":
            f"The highest recorded sale is ₹{highest_sale:,.2f}."

    })

# =====================================================
# PROFIT INSIGHTS
# =====================================================

def generate_profit_insights(df, insights):

    profit_column = find_column(
        df,
        ["profit", "income"]
    )

    if profit_column is None:
        return

    total_profit = df[profit_column].sum()

    avg_profit = df[profit_column].mean()

    loss_rows = (df[profit_column] < 0).sum()

    insights.append({

        "type": "summary",

        "title": "Total Profit",

        "description":
            f"Overall profit equals ₹{total_profit:,.2f}."

    })

    insights.append({

        "type": "summary",

        "title": "Average Profit",

        "description":
            f"Average profit per transaction is ₹{avg_profit:,.2f}."

    })

    if loss_rows > 0:

        insights.append({

            "type": "warning",

            "title": "Loss Making Orders",

            "description":
                f"{loss_rows:,} transactions resulted in a loss."

        })

    else:

        insights.append({

            "type": "success",

            "title": "Profitability",

            "description":
                "No loss-making transactions were found."

        })
# =====================================================
# DISCOUNT INSIGHTS
# =====================================================

def generate_discount_insights(df, insights):

    discount_column = find_column(
        df,
        ["discount"]
    )

    if discount_column is None:
        return

    average_discount = df[discount_column].mean()

    maximum_discount = df[discount_column].max()

    insights.append({

        "type": "info",

        "title": "Average Discount",

        "description":
            f"Average discount offered is {average_discount:.2f}."

    })

    insights.append({

        "type": "info",

        "title": "Maximum Discount",

        "description":
            f"Maximum recorded discount is {maximum_discount:.2f}."

    })

# =====================================================
# CATEGORY INSIGHTS
# =====================================================

def generate_category_insights(df, insights):

    category_column = find_column(
        df,
        ["category"]
    )

    sales_column = find_column(
        df,
        ["sales", "revenue", "amount"]
    )

    if category_column is None:
        return

    top_category = (
        df[category_column]
        .value_counts()
        .idxmax()
    )

    insights.append({

        "type": "summary",

        "title": "Top Category",

        "description":
            f"'{top_category}' appears most frequently in the dataset."

    })

    if sales_column:

        category_sales = (

            df.groupby(category_column)[sales_column]

            .sum()

            .sort_values(ascending=False)

        )

        best = category_sales.index[0]

        worst = category_sales.index[-1]

        insights.append({

            "type": "success",

            "title": "Best Performing Category",

            "description":
                f"{best} generated the highest sales."

        })

        insights.append({

            "type": "warning",

            "title": "Lowest Performing Category",

            "description":
                f"{worst} generated the lowest sales."

        })

# =====================================================
# MAIN FUNCTION
# =====================================================

def generate_insights(
    df: pd.DataFrame,
    dataset_profile: dict,
    cleaning_summary: dict,
    eda: dict
):

    insights = []

    # Dataset Summary
    generate_dataset_summary(
        df,
        dataset_profile,
        cleaning_summary,
        insights
    )

    # Missing Values
    generate_missing_value_insights(
        dataset_profile,
        insights
    )

    # Duplicate Rows
    generate_duplicate_insights(
        cleaning_summary,
        insights
    )

    # Sales Analysis
    generate_sales_insights(
        df,
        insights
    )

    # Profit Analysis
    generate_profit_insights(
        df,
        insights
    )

    # Discount Analysis
    generate_discount_insights(
        df,
        insights
    )

    # Category Analysis
    generate_category_insights(
        df,
        insights
    )

    return insights