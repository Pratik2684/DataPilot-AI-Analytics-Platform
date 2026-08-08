def generate_pandas(prompt):

    if not prompt:
        return "# Enter a pandas task."

    text = prompt.lower()

    # ==========================================
    # Missing Values
    # ==========================================

    if "remove missing" in text or "drop missing" in text:

        return """df = df.dropna()"""

    elif "fill missing" in text:

        return """df = df.fillna(0)"""

    elif "check missing" in text or "missing values" in text:

        return """df.isnull().sum()"""

    # ==========================================
    # Duplicate Rows
    # ==========================================

    elif "duplicate" in text:

        return """df = df.drop_duplicates()"""

    # ==========================================
    # Summary Statistics
    # ==========================================

    elif "summary" in text or "describe" in text:

        return """df.describe(include='all')"""

    # ==========================================
    # Head
    # ==========================================

    elif "head" in text:

        return """df.head()"""

    # ==========================================
    # Tail
    # ==========================================

    elif "tail" in text:

        return """df.tail()"""

    # ==========================================
    # Shape
    # ==========================================

    elif "shape" in text:

        return """df.shape"""

    # ==========================================
    # Columns
    # ==========================================

    elif "columns" in text:

        return """df.columns"""

    # ==========================================
    # Correlation
    # ==========================================

    elif "correlation" in text:

        return """df.corr(numeric_only=True)"""

    # ==========================================
    # Value Counts
    # ==========================================

    elif "value count" in text:

        return """df['Column_Name'].value_counts()"""

    # ==========================================
    # Sort
    # ==========================================

    elif "sort" in text:

        return """df.sort_values(by='Column_Name', ascending=False)"""

    # ==========================================
    # Group By
    # ==========================================

    elif "group by" in text:

        return """df.groupby('Column_Name').mean(numeric_only=True)"""

    # ==========================================
    # Filter
    # ==========================================

    elif "filter" in text:

        return """df[df['Column_Name'] == 'Value']"""

    # ==========================================
    # Select Columns
    # ==========================================

    elif "select column" in text:

        return """df[['Column1', 'Column2']]"""

    # ==========================================
    # Default
    # ==========================================

    return """
# Task not recognized.

# Example prompts:

Remove Missing Values

Fill Missing Values

Drop Duplicates

Summary Statistics

Shape

Columns

Correlation

Value Counts

Sort Data

Group By Department

Filter Rows

Select Columns
"""