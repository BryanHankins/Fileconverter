import argparse
import os

def convert_docx_to_pdf(input_file, output_file):
    command = f'libreoffice --headless --convert-to pdf --outdir {os.path.dirname(output_file)} {input_file}'
    os.system(command)
    print(f'Conversion complete: {input_file} to {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert DOCX to PDF')
    parser.add_argument('input', help='Input DOCX file')
    parser.add_argument('output', help='Output PDF file')
    args = parser.parse_args()
    convert_docx_to_pdf(args.input, args.output)