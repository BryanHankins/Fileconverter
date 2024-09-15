
import pandas as pd

def convert_csv_to_excel(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_excel(output_file, index=False)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

def convert_excel_to_csv(input_file, output_file):
    df = pd.read_excel(input_file)
    df.to_csv(output_file, index=False)
    print('Conversion complete: {} to {}'.format(input_file, output_file))
