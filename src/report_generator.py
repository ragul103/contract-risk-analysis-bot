from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_pdf(report_lines, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 40
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Contract Risk Analysis Report")
    y -= 30

    c.setFont("Helvetica", 10)

    for line in report_lines:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 40

        c.drawString(40, y, line)
        y -= 14

    c.save()
