import pandas as pd

def ask_ai(question, df):

    question = question.lower()

    if "rows" in question:
        return f"The dataset contains {df.shape[0]} rows."

    elif "columns" in question:
        return f"The dataset contains {df.shape[1]} columns."

    elif "missing" in question:
        return df.isnull().sum().to_string()

    elif "duplicate" in question:
        return f"Duplicate Rows: {df.duplicated().sum()}"

    elif "highest salary" in question:

        if "Salary" in df.columns:
            row = df.loc[df["Salary"].idxmax()]
            return row.to_string()

        return "Salary column not found."

    elif "average salary" in question:

        if "Salary" in df.columns:
            return f"Average Salary = {df['Salary'].mean():,.2f}"

        return "Salary column not found."

    elif "recommend chart" in question:

        return """
Recommended Charts

• Bar Chart
• Pie Chart
• Histogram
• Scatter Plot
• Box Plot
"""

    elif "sql" in question:

        return """
SELECT *
FROM employees
WHERE Salary >
(
SELECT AVG(Salary)
FROM employees
);
"""

    elif "pandas" in question:

        return """
df.drop_duplicates()

df.fillna(0)

df.describe()

df.groupby('Department')['Salary'].mean()
"""

    elif "summary" in question:

        return f"""
Dataset Summary

Rows : {df.shape[0]}
Columns : {df.shape[1]}
Missing Values : {df.isnull().sum().sum()}
Duplicate Rows : {df.duplicated().sum()}
"""

    else:

        return """
I can answer questions about:

• Missing Values
• Duplicate Rows
• Highest Salary
• Average Salary
• SQL Queries
• Pandas Code
• Chart Recommendation
• Dataset Summary
"""