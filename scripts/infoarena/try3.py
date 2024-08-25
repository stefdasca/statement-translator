import os
import re

# Directory containing the text files
input_dir = 'infoarena'  # Change this to your directory

keywords = [
    "Cerinţă", "Date de intrare", "Date de ieşire", "Restricţii",
    "Exemplu", "Exemple", "Explicaţie", "Explicaţii", "Explicatie", "Explicatii", "Cerinta", "Date de iesire", "Restrictii"
]
def process_file(file_path):
    # Create 'outputs' folder if it doesn't exist
    output_folder = 'outputs'
    os.makedirs(output_folder, exist_ok=True)

    # Get the base name of the file (without the directory path)
    base_name = os.path.basename(file_path)
    # Generate the new file name by adding '-final' before '.txt'
    base, ext = os.path.splitext(base_name)
    final_file_name = f"{base}{ext}"

    # Construct the final file path inside the 'outputs' folder
    final_file_path = os.path.join(output_folder, final_file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize an empty string to accumulate the merged content
    merged_string = ''

    # Process the lines
    if lines:
        # Add newline after the first line
        merged_string += lines[1].strip() + '\n' + '\n'

        for line in lines[2:]:
            stripped_line = line.strip()

            # Check if any keyword is present in the line
            if any(keyword in stripped_line for keyword in keywords):
                # If a keyword is found, separate it and add double newline
                merged_string += '\n\n' + stripped_line + '\n\n'
            else:
                # Otherwise, just add the line with a space at the end
                merged_string += stripped_line + ' '

    # Write the processed lines back to the new file in the 'outputs' folder
    with open(final_file_path, 'w', encoding='utf-8') as file:
        file.write(merged_string)

    return merged_string, final_file_path

def main():
    # Process each text file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing {file_path}...")
            process_file(file_path)
            print(f"Finished processing {file_path}")

if __name__ == "__main__":
    main()
