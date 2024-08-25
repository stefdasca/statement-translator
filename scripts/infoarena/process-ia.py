import os
import re

# Directory containing the text files
input_dir = 'infoarena'  # Change this to your directory

# Keywords to check for adding '##'
keywords = [
    "Cerinţă", "Date de intrare", "Date de ieşire", "Restricţii",
    "Exemplu", "Exemple", "Explicaţie", "Explicaţii"
]

# Sections that should not have merged lines
no_merge_sections = ["Restricţii", "Exemplu", "Exemple"]

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    current_text_block = []
    merging_allowed = True  # Initially allow merging
    first_non_empty_found = False

    # Step 1: Loop through each line to process formatting
    for line in lines:
        # Strip whitespace but keep original line for re-insertion if needed
        stripped_line = line.strip()

        # If the line is non-empty (i.e., has at least one letter)
        if not first_non_empty_found and re.search(r'[a-zA-Z]', stripped_line):
            processed_lines.append(line.rstrip())  # First non-empty line
            processed_lines.append("\n")  # Add new line after the first non-empty line
            processed_lines.append("\n")  # Add new line after the first non-empty line
            first_non_empty_found = True
            continue

        # Handle keywords that require ## before and after them
        if any(keyword in stripped_line for keyword in keywords):
            if current_text_block:
                if merging_allowed:
                    processed_lines.append(" ".join(current_text_block) + "\n")
                else:
                    processed_lines.extend([block + "\n" for block in current_text_block])
                current_text_block = []

            # Add newlines around the keyword
            processed_lines.append("\n\n## " + stripped_line + "\n\n")

            # Check if merging should be disabled for this section
            in_no_merge_section = any(keyword in stripped_line for keyword in no_merge_sections)
            merging_allowed = not in_no_merge_section

            continue

        # If we are not in a no-merge section, accumulate lines for merging
        if merging_allowed:
            current_text_block.append(stripped_line)
        else:
            # Add lines directly without merging
            processed_lines.append(line.rstrip() + "\n")

    # Merge the last block of text if applicable
    if current_text_block and merging_allowed:
        processed_lines.append(" ".join(current_text_block) + "\n")
    elif current_text_block:
        processed_lines.extend([block + "\n" for block in current_text_block])
    print(processed_lines)

    # Step 2: Add a new line after every usage of a period (.), except when followed by "out" or "in"
    final_lines = []
    for line in processed_lines:
        if "..." in line:
            final_lines.append(line)
            continue

        # Find all periods and handle exceptions for "in" and "out"
        parts = re.split(r'(\.\s*)', line)
        for i in range(len(parts) - 1):
            print(parts[i] + "x")
            if parts[i].strip().endswith('.') and i + 1 < len(parts):
                pos = i+1
                next_word = parts[i + 1].strip().split()[0] if parts[i + 1].strip() else ''
                while pos + 1 < len(parts) and not next_word:
                    pos += 1
                    next_word = parts[pos].strip().split()[0] if parts[pos].strip() else ''
                print(next_word)
                if next_word not in ['in', 'out'] and (not next_word or (not next_word[0].isdigit() and not next_word[0] == '-' and len(next_word) >= 3)):
                    final_lines.append(parts[i].strip() + "\n\n")
                else:
                    final_lines.append(parts[i] + parts[i + 1])
                    i += 1  # Skip the next part because we already added it
            else:
                final_lines.append(parts[i])
        if parts[-1]:
            final_lines.append(parts[-1])

    # Write the processed lines back to the file (or a new file)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(final_lines)

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
