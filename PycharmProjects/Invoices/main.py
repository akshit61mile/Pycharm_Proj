import pandas as pd
import glob
from fpdf import FPDF
from pathlib import  Path

filepaths = glob.glob("Invoice/.*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",unit="mm",format="A4",)
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times",size=8, style = "B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"pdfs/{filename}.pdf")


