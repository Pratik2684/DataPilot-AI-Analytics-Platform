import pandas as pd


def generate_insights(df):

    insights = []

    # =====================================
    # Dataset Information
    # =====================================

    insights.append(f"📊 Total Rows : {df.shape[0]}")
    insights.append(f"📋 Total Columns : {df.shape[1]}")

    # =====================================
    # Missing Values
    # =====================================

    missing = int(df.isnull().sum().sum())

    if missing == 0:
        insights.append("✅ No missing values found.")
    else:
        insights.append(f"⚠ {missing} missing values detected.")

    # =====================================
    # Duplicate Rows
    # =====================================

    duplicates = int(df.duplicated().sum())

    if duplicates == 0:
        insights.append("✅ No duplicate rows found.")
    else:
        insights.append(f"⚠ {duplicates} duplicate rows detected.")

    # =====================================
    # Numeric Columns
    # =====================================

    numeric = df.select_dtypes(include="number").columns

    insights.append(f"🔢 Numeric Columns : {len(numeric)}")

    # =====================================
    # Categorical Columns
    # =====================================

    categorical = df.select_dtypes(exclude="number").columns

    insights.append(f"🔤 Categorical Columns : {len(categorical)}")

    # =====================================
    # Salary Analysis
    # =====================================

    if "Salary" in df.columns:

        insights.append(
            f"💰 Average Salary : ₹{df['Salary'].mean():,.0f}"
        )

        insights.append(
            f"💰 Maximum Salary : ₹{df['Salary'].max():,.0f}"
        )

        insights.append(
            f"💰 Minimum Salary : ₹{df['Salary'].min():,.0f}"
        )

    # =====================================
    # Experience Analysis
    # =====================================

    if "Experience" in df.columns:

        insights.append(
            f"👨‍💼 Average Experience : {df['Experience'].mean():.1f} Years"
        )

    # =====================================
    # Age Analysis
    # =====================================

    if "Age" in df.columns:

        insights.append(
            f"🎂 Average Age : {df['Age'].mean():.1f}"
        )

    # =====================================
    # Largest Category
    # =====================================

    for col in categorical:

        try:

            top = df[col].mode()[0]

            count = df[col].value_counts().iloc[0]

            insights.append(
                f"🏆 Most Common {col}: {top} ({count} records)"
            )

        except:
            pass

    # =====================================
    # Data Quality
    # =====================================

    score = 100

    score -= min(missing, 30)

    score -= min(duplicates * 5, 20)

    score = max(score, 0)

    if score >= 90:

        insights.append("🟢 Dataset Quality : Excellent")

    elif score >= 70:

        insights.append("🟡 Dataset Quality : Good")

    else:

        insights.append("🔴 Dataset Quality : Needs Cleaning")

    # =====================================
    # Recommendations
    # =====================================

    insights.append("")

    insights.append("💡 Recommendations")

    if missing > 0:
        insights.append("• Fill missing values before analysis.")

    if duplicates > 0:
        insights.append("• Remove duplicate rows.")

    if len(numeric) > 3:
        insights.append("• Build a correlation heatmap.")

    if len(categorical) > 2:
        insights.append("• Compare categorical columns using bar charts.")

    if missing == 0 and duplicates == 0:
        insights.append("• Dataset is ready for Machine Learning.")

    return insights