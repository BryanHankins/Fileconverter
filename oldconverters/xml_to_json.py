
import xmltodict
import json

def convert_xml_to_json(input_file, output_file):
    with open(input_file) as f:
        xml_content = f.read()
    json_content = xmltodict.parse(xml_content)
    with open(output_file, 'w') as f:
        json.dump(json_content, f, indent=4)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

def convert_json_to_xml(input_file, output_file):
    with open(input_file) as f:
        json_content = json.load(f)
    xml_content = xmltodict.unparse(json_content, pretty=True)
    with open(output_file, 'w') as f:
        f.write(xml_content)
    print('Conversion complete: {} to {}'.format(input_file, output_file))
