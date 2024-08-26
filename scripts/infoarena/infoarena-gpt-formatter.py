import openai
import os

openai.api_key = "ADD-YOUR-API-KEY"

def generate_gpt_response(user_text, model_name="gpt-4o", print_output=False):
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_text}],
            max_tokens=3000
        )
        text_output = response['choices'][0]['message']['content'] if response['choices'] else "No response generated."
        if print_output:
            print(text_output)
        return text_output
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        s = file.read()
        s1 = s.replace("≤", "\\leq")
        return s1

def save_to_file(content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def clean_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = content.strip('`')
    cleaned_content = cleaned_content.removeprefix("markdown")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

file_pattern = '.md'
def convert_format():
    base_path = './outputs/'
    base_path2 = './infoarena format/'
    for filename in os.listdir(base_path):
        input_file_path = os.path.join(base_path, filename)
        file_name, _ = os.path.splitext(filename)
        file_contents = read_file(input_file_path)
        processing_request = r"You are given a competitive programming problem statement in Romanian. Please add ## and a space before the following Romanian key words or expressions mentioned here: Cerinţă, Date de intrare, Date de ieşire, Restricţii, Exemplu, Exemple, Explicaţie, Explicaţii, Explicatie, Explicatii, Cerinta, Date de iesire, Restrictii. Cover variables, expressions and numbers using markdown syntax, with $. For various signs, replace them with the latex equivalent. Avoid double consecutive $ in expressions (just write one of them if they are part of the same expression. For the three dots, use $\dots$ instead.  If you see multiple constraints on the same line, split them along multiple lines. For example data, add the input and output within backticks. Do not add any personal comments, or remarks, just process the problem. Do not add double dollar signs, keep the singular dollar sign"
        prompt = f"{processing_request}\n\nAfter this line you will find the statement\n\n{file_contents}"
        response = generate_gpt_response(prompt)
        output_file_path = os.path.join(base_path2, f'{file_name}.md')
        save_to_file(response, output_file_path)
        clean_markdown_file(output_file_path)
        print(f"Processed {input_file_path} and saved response to {output_file_path}")
        # break

def translate():
    base_path = './infoarena format/'
    base_path2 = './infoarena-md/'
    for filename in os.listdir(base_path):
        input_file_path = os.path.join(base_path, filename)
        file_name, _ = os.path.splitext(filename)
        file_contents = read_file(input_file_path)
        processing_request = "Please process the following text according to the specified instructions: You will be given a competitive programming problem statement in markdown, written in the Romanian language, using GFM extensions and MathJax/LaTeX math between dollar signs ($ or $$). Another extension is the fact that image attachments are defined using a syntax similar to ~[name.png], with optional attributes named after the end with a vertical bar ('|'). You must translate the statement in the English language, while preserving mathematical values, variable names, general syntax, structure and format. You must also preserve the custom image format exactly as is. The word Cerință task is always translated to Task, Date de intrare is translated to Input data, Date de ieșire is translated to Output data, subsecvență is translated to subarray, subșir is translated to subsequence, Restricții și precizări to Constraints and clarifications, vector is translated to array. In addition, in the Date de intrare and Date de ieșire sections, if you see expressions such as Pe prima linie, Pe a doua linie etc., you want to use the verb contain to describe the data we need to read or print. In the Date de ieșire sections, you can also use the verb print to describe the data we need to print. When separating large integers (especially in latex/mathjax math) in groups of 3 digits, do not add a comma. Instead, add a backslash followed and preceded by a single space character. After you are done with translating, please double check the statement and fix potential grammar and/or syntax errors according to the rules of English language. Do not translate any strings in the example inputs and outputs"
        prompt = f"{processing_request}\n\nAfter this line you will find the statement\n\n{file_contents}"
        response = generate_gpt_response(prompt)
        output_file_path = os.path.join(base_path2, f'{file_name}.md')
        save_to_file(response, output_file_path)
        print(f"Processed {input_file_path} and saved response to {output_file_path}")
        # break

convert_format()
# translate()






