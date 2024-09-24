from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm', format='A4')

df = pd.read_csv('topics.csv')

# To create a single page
# pdf.add_page()
# pdf.set_font(family='Times', style='B', size=12)
# pdf.cell(w=5, h=12,txt="Hello Mumbai", align='C', ln=1, border=1)
# pdf.cell(w=0, h=12,txt="Hello Pune", align='C', ln=1, border=1)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(254,0,0)
    pdf.cell(w=0, h=12,txt=row["Topic"], align='L', ln=1)
    pdf.line(10,22,200, 22)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

# Create multiple pdf
pdf.output("output.pdf" "")
