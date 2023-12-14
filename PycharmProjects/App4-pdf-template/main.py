from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics1.csv")

for index,row in df.iterrows():
    pdf.add_page()

    #Header
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=0, h=12, align="L",txt=row["Topic"],ln=1)
    pdf.set_text_color(0,0,254)
    pdf.line(20,30,20,30)

    #Footer
    pdf.ln(265)
    pdf.set_font(family="Times", size=8, style="I")
    pdf.cell(w=0, h=10, align="L", txt=row["Topic"], ln=1)
    pdf.set_text_color(180, 180, 180)



    for i in range(row["Pages"]-1):
        pdf.add_page()

        #Footer
        pdf.ln(265)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.cell(w=0, h=10, align="L", txt=row["Topic"], ln=1)
        pdf.set_text_color(180, 180, 180)

pdf.output("output.pdf")
