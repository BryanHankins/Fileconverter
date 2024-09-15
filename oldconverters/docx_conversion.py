
from docx2pdf import convert
import pypandoc

def convert_docx(input_file, output_file, output_format):
    valid_formats = ['odt', 'rtf']
    if output_format not in valid_formats:
        print('Invalid output format! Supported formats are: {}'.format(valid_formats))
        return
    pypandoc.convert_file(input_file, output_format, outputfile=output_file)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

# Example usage for valid formats
convert_docx('./Docx/test_document.docx', 'test_document.odt', 'odt')
convert_docx('./Docx/test_document.docx', 'test_document.rtf', 'rtf')
