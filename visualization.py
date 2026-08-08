import plotly.express as px


# ==========================================
# Dynamic Chart Generator
# ==========================================

def create_chart(df, chart_type, x_col=None, y_col=None):

    try:

        if chart_type == "Bar Chart":
            return px.bar(
                df,
                x=x_col,
                y=y_col,
                color=x_col,
                title="Bar Chart"
            )

        elif chart_type == "Line Chart":
            return px.line(
                df,
                x=x_col,
                y=y_col,
                title="Line Chart"
            )

        elif chart_type == "Scatter Plot":
            return px.scatter(
                df,
                x=x_col,
                y=y_col,
                title="Scatter Plot"
            )

        elif chart_type == "Histogram":
            return px.histogram(
                df,
                x=x_col,
                title="Histogram"
            )

        elif chart_type == "Pie Chart":
            return px.pie(
                df,
                names=x_col,
                title="Pie Chart"
            )

        elif chart_type == "Box Plot":
            return px.box(
                df,
                x=x_col,
                y=y_col,
                title="Box Plot"
            )

        elif chart_type == "Heatmap":

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

    except Exception:
        return None

    return None


# ==========================================
# AI Chart Recommendation Engine
# ==========================================

def chart_recommendations(df):

    recommendations = []

    numeric = df.select_dtypes(include="number").columns

    categorical = df.select_dtypes(exclude="number").columns

    for col in numeric:

        recommendations.append(
            f"📈 Histogram recommended for '{col}'"
        )

        recommendations.append(
            f"📦 Box Plot recommended for '{col}'"
        )

    for col in categorical:

        recommendations.append(
            f"📊 Bar Chart recommended for '{col}'"
        )

        recommendations.append(
            f"🥧 Pie Chart recommended for '{col}'"
        )

    return recommendations