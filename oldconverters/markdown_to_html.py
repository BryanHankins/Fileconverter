
import markdown

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(output_file, 'w') as f:
        f.write(html)
    print('Conversion complete: {} to {}'.format(input_file, output_file))

def convert_html_to_markdown(input_file, output_file):
    import markdown2
    with open(input_file, 'r') as f:
        html = f.read()
    markdown_text = markdown2.markdown(html)
    with open(output_file, 'w') as f:
        f.write(markdown_text)
    print('Conversion complete: {} to {}'.format(input_file, output_file))
