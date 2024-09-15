
from PIL import Image

def convert_image(input_file, output_file):
    with Image.open(input_file) as img:
        img.convert('RGB').save(output_file, 'JPEG')
    print('Conversion complete: {} to {}'.format(input_file, output_file))

# Example usage for PNG to JPG conversion
convert_image('FileConverter/sample_image.png', 'FileConverter/sample_image.jpg')
