import os

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        s = file.read()
        s1 = s.replace("≤", "\\leq")
        return s1.encode('utf-8')

def clean_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = content.strip('`')
    cleaned_content = cleaned_content.removeprefix("markdown")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def save_to_file(content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

base_path = './Markdown statements/CerinteEN/'
file_pattern = '{}.md'

for i in range(11, 2911):
    file_number = f"Processed_{i:04d}"
    input_file_path = os.path.join(base_path, file_pattern.format(file_number))
    print(input_file_path)
    if os.path.exists(input_file_path):
        clean_markdown_file(input_file_path)
        file_contents = read_file(input_file_path)
        print(file_contents)
