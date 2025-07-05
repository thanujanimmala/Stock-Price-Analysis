from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Stock Price Analysis Report", ln=True, align="C")

        self.ln(10)

    def add_plot(self, title, image_path):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.image(image_path, w=180)
        self.ln(10)

def generate_pdf(ticker, start, end, image_paths, output_path="report.pdf"):
    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Stock: {ticker}", ln=True)
    pdf.cell(0, 10, f"Date Range: {start} to {end}", ln=True)
    pdf.ln(5)
    

    for title, img_path in image_paths:
        if os.path.exists(img_path):
            pdf.add_plot(title, img_path)

    pdf.output(output_path)
    return output_path
