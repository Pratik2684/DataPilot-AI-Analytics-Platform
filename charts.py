import plotly.express as px


# ==========================================
# Bar Chart
# ==========================================

def bar_chart(df):

    numeric = df.select_dtypes(include="number").columns
    categorical = df.select_dtypes(exclude="number").columns

    if len(numeric) == 0 or len(categorical) == 0:
        return None

    return px.bar(
        df,
        x=categorical[0],
        y=numeric[0],
        color=categorical[0],
        title="Bar Chart"
    )


# ==========================================
# Pie Chart
# ==========================================

def pie_chart(df):

    categorical = df.select_dtypes(exclude="number").columns

    if len(categorical) == 0:
        return None

    counts = df[categorical[0]].value_counts().reset_index()
    counts.columns = ["Category", "Count"]

    return px.pie(
        counts,
        names="Category",
        values="Count",
        title="Pie Chart"
    )


# ==========================================
# Histogram
# ==========================================

def histogram(df):

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) == 0:
        return None

    return px.histogram(
        df,
        x=numeric[0],
        title="Histogram"
    )


# ==========================================
# Scatter Plot
# ==========================================

def scatter(df):

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) < 2:
        return None

    return px.scatter(
        df,
        x=numeric[0],
        y=numeric[1],
        title="Scatter Plot"
    )


# ==========================================
# Box Plot
# ==========================================

def box_plot(df):

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) == 0:
        return None

    return px.box(
        df,
        y=numeric[0],
        title="Box Plot"
    )


# ==========================================
# Heatmap
# ==========================================

def heatmap(df):

    numeric = df.select_dtypes(include="number")

    if numeric.shape[1] < 2:
        return None

    corr = numeric.corr()

    return px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Blues",
        title="Correlation Heatmap"
    )


# ==========================================
# Line Chart
# ==========================================

def line_chart(df):

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) < 2:
        return None

    return px.line(
        df,
        x=numeric[0],
        y=numeric[1],
        title="Line Chart"
    )