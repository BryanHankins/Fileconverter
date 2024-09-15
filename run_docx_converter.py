import subprocess

# Function to run the DOCX to PDF converter
def run_converter(input_file, output_file):
    command = ['./Executable/docx_converter', input_file, output_file]
    subprocess.run(command)

if __name__ == '__main__':
    input_file = './Docx/test_document.docx'
    output_file = './Docx/test_document.pdf'
    run_converter(input_file, output_file)