from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(df):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>DataPilot AI Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(f"Rows : {df.shape[0]}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"Columns : {df.shape[1]}", styles["Normal"])
    )

    elements.append(
        Paragraph(
            f"Missing Values : {df.isnull().sum().sum()}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Duplicate Rows : {df.duplicated().sum()}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer