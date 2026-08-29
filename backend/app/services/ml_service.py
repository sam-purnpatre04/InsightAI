import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from sklearn.impute import SimpleImputer

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ======================================================
# TARGET DETECTION
# ======================================================

def detect_target_column(df: pd.DataFrame):

    """
    Attempts to identify a suitable target column.

    Strategy:
    1. Prefer columns with names commonly used as targets.
    2. Otherwise use a low-cardinality categorical column.
    """

    target_keywords = [
        "target",
        "label",
        "outcome",
        "default",
        "status",
        "churn",
        "approved",
        "approval",
        "fraud",
        "risk",
        "price",
        "sales",
        "revenue"
    ]

    # ------------------------------------------
    # Search by column name
    # ------------------------------------------

    for column in df.columns:

        column_lower = column.lower()

        for keyword in target_keywords:

            if keyword in column_lower:

                return column


    # ------------------------------------------
    # Search for low-cardinality columns
    # ------------------------------------------

    categorical_columns = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns

    for column in categorical_columns:

        unique_values = df[column].nunique()

        if 2 <= unique_values <= 10:

            return column


    return None


# ======================================================
# DETECT PROBLEM TYPE
# ======================================================

def detect_problem_type(df: pd.DataFrame, target_column):

    """
    Determines whether the ML problem is classification
    or regression.
    """

    target = df[target_column]

    # Categorical target
    if (
        target.dtype == "object"
        or str(target.dtype) == "category"
        or target.dtype == "bool"
    ):

        return "classification"


    # Numeric target with small number of unique values
    if target.nunique() <= 10:

        return "classification"


    return "regression"


# ======================================================
# BUILD PREPROCESSOR
# ======================================================

def build_preprocessor(X):

    """
    Builds preprocessing pipeline for numerical
    and categorical features.
    """

    numerical_columns = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = X.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()


    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            )
        ]
    )


    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )


    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        ]
    )


    return preprocessor


# ======================================================
# CLASSIFICATION
# ======================================================

def run_classification(df, target_column):

    data = df.copy()

    data = data.dropna(
        subset=[target_column]
    )


    X = data.drop(
        columns=[target_column]
    )

    y = data[target_column]


    if X.shape[1] == 0:

        return {
            "status": "failed",
            "message": "No features available for ML."
        }


    if y.nunique() < 2:

        return {
            "status": "failed",
            "message": "Target column contains fewer than two classes."
        }


    preprocessor = build_preprocessor(X)


    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )


    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )


    try:

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

    except ValueError:

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )


    pipeline.fit(
        X_train,
        y_train
    )


    predictions = pipeline.predict(
        X_test
    )


    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )


    return {

        "status": "success",

        "problem_type": "classification",

        "model": "Random Forest Classifier",

        "target_column": target_column,

        "training_rows": len(X_train),

        "testing_rows": len(X_test),

        "classes": int(y.nunique()),

        "accuracy": round(
            accuracy * 100,
            2
        ),

        "precision": round(
            precision * 100,
            2
        ),

        "recall": round(
            recall * 100,
            2
        ),

        "f1_score": round(
            f1 * 100,
            2
        )
    }


# ======================================================
# REGRESSION
# ======================================================

def run_regression(df, target_column):

    data = df.copy()

    data = data.dropna(
        subset=[target_column]
    )


    X = data.drop(
        columns=[target_column]
    )

    y = data[target_column]


    if not pd.api.types.is_numeric_dtype(y):

        return {
            "status": "failed",
            "message": "Regression target must be numeric."
        }


    if X.shape[1] == 0:

        return {
            "status": "failed",
            "message": "No features available for ML."
        }


    preprocessor = build_preprocessor(X)


    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )


    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                model
            )
        ]
    )


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    pipeline.fit(
        X_train,
        y_train
    )


    predictions = pipeline.predict(
        X_test
    )


    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )


    return {

        "status": "success",

        "problem_type": "regression",

        "model": "Random Forest Regressor",

        "target_column": target_column,

        "training_rows": len(X_train),

        "testing_rows": len(X_test),

        "mae": round(
            mae,
            4
        ),

        "rmse": round(
            rmse,
            4
        ),

        "r2_score": round(
            r2,
            4
        )
    }


# ======================================================
# MAIN ML FUNCTION
# ======================================================

def generate_ml_analysis(df: pd.DataFrame):

    """
    Main ML analysis pipeline.
    """

    if df.empty:

        return {
            "status": "failed",
            "message": "Dataset is empty."
        }


    if len(df) < 20:

        return {
            "status": "skipped",
            "message": "Dataset is too small for reliable ML analysis."
        }


    target_column = detect_target_column(df)


    if target_column is None:

        return {
            "status": "skipped",

            "message": (
                "No suitable target column "
                "could be automatically detected."
            )
        }


    problem_type = detect_problem_type(
        df,
        target_column
    )


    if problem_type == "classification":

        return run_classification(
            df,
            target_column
        )


    return run_regression(
        df,
        target_column
    )