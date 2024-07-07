import os

def read_file(file_path):
    """Read the contents of a file and return as a string."""
    with open(file_path, 'r', encoding='cp1252', errors="ignore") as file:
        s = file.read()
        s1 = s.replace("≤", "\\leq")
        return s1.encode('utf-8')

def clean_markdown_file(file_path):
    with open(file_path, 'r', encoding='cp1252', errors="ignore") as file:
        content = file.read()

    cleaned_content = content.strip('`')
    cleaned_content = cleaned_content.removeprefix("markdown")

    # Replace \( with $ and \) with $
    cleaned_content = cleaned_content.replace('\\(', '$').replace('\\)', '$')
    cleaned_content = cleaned_content.replace('<=', '\\leq')
    cleaned_content = cleaned_content.replace('>=', '\\geq')

    with open(file_path, 'w', encoding='cp1252', errors="ignore") as file:
        file.write(cleaned_content)

def save_to_file(content, output_file_path):
    """Save the given content to a file."""
    with open(output_file_path, 'w', encoding='cp1252', errors="ignore") as file:
        file.write(content)

# Example usage

base_path = './Markdown statements/CerinteEN/'
file_pattern = '{}.md'

for i in range(0, 2911):  # Loop through numbers 1 to 9999
    file_number = f"Processed_{i:04d}"  # Format number as a 4-digit string
    input_file_path = os.path.join(base_path, file_pattern.format(file_number))
    print(input_file_path)
    if os.path.exists(input_file_path):
        clean_markdown_file(input_file_path)
        file_contents = read_file(input_file_path)
        print(file_contents)
