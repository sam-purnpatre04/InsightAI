import pandas as pd


def read_csv(upload_file):
    df = pd.read_csv(upload_file.file)

    return {
        "filename": upload_file.filename,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": df.columns.tolist()
    }