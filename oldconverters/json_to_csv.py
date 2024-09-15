
import pandas as pd

def convert_json_to_csv(input_file, output_file):
    df = pd.read_json(input_file)
    df.to_csv(output_file, index=False)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

def convert_csv_to_json(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_json(output_file, orient='records', lines=True)
    print('Conversion complete: {} to {}'.format(input_file, output_file))
