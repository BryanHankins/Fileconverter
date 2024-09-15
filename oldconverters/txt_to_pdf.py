
from fpdf import FPDF

def convert_txt_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    with open(input_file, 'r') as f:
        for line in f:
            pdf.cell(200, 10, txt=line, ln=True)
    pdf.output(output_file)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

def convert_pdf_to_txt(input_file, output_file):
    from PyPDF2 import PdfReader
    reader = PdfReader(input_file)
    with open(output_file, 'w') as f:
        for page in reader.pages:
            f.write(page.extract_text())
    print('Conversion complete: {} to {}'.format(input_file, output_file))
