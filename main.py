from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

# To create a single page
# pdf.add_page()
# pdf.set_font(family='Times', style='B', size=12)
# pdf.cell(w=5, h=12,txt="Hello Mumbai", align='C', ln=1, border=1)
# pdf.cell(w=0, h=12,txt="Hello Pune", align='C', ln=1, border=1)

for index, row in df.iterrows():
    # Set header for master page
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12,txt=row["Topic"], align='L', ln=1)
    # Adding line to master page
    for y in range(20, 290, 10):
        pdf.line(10,y,200, y)

    # Set footer for master page
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Set footer for subpage
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)

        # Adding line to subpages
        for y in range(10, 290, 10):
            pdf.line(10, y, 200, y)

# Create multiple pdf
pdf.output("output.pdf" "")
print("Done")