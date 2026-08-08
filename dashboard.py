import pandas as pd


def get_kpis(df):

    kpis = {}

    # ==========================================
    # Basic KPIs
    # ==========================================

    kpis["rows"] = df.shape[0]

    kpis["columns"] = df.shape[1]

    kpis["missing"] = int(df.isnull().sum().sum())

    kpis["duplicates"] = int(df.duplicated().sum())

    # ==========================================
    # Data Types
    # ==========================================

    kpis["numeric"] = len(
        df.select_dtypes(include="number").columns
    )

    kpis["categorical"] = len(
        df.select_dtypes(exclude="number").columns
    )

    # ==========================================
    # Memory Usage
    # ==========================================

    kpis["memory"] = round(
        df.memory_usage(deep=True).sum() / 1024,
        2
    )

    # ==========================================
    # Data Quality Score
    # ==========================================

    score = 100

    score -= min(kpis["missing"], 30)

    score -= min(kpis["duplicates"] * 5, 20)

    kpis["quality_score"] = max(score, 0)

    # ==========================================
    # Optional KPIs
    # ==========================================

    if "Salary" in df.columns:

        kpis["avg_salary"] = round(
            df["Salary"].mean(),
            2
        )

        kpis["max_salary"] = round(
            df["Salary"].max(),
            2
        )

    else:

        kpis["avg_salary"] = None

        kpis["max_salary"] = None

    if "Experience" in df.columns:

        kpis["avg_experience"] = round(
            df["Experience"].mean(),
            2
        )

    else:

        kpis["avg_experience"] = None

    return kpis