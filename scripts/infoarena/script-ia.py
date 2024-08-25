import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# List of links (URLs) to process

urls_file = 'listproblems-monthly.txt'

# Directory to save text files
output_dir = './infoarena/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def fetch_page_content(url):
    # Fetch the page HTML content
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page: {url}, Error: {e}")
        return None


def extract_text_from_html(html_content):
    # Parse HTML and extract text content
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator="\n", strip=True)


def save_text_to_file(text, filename):
    # Write text content to a text file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
def get_problem_name_from_url(url):
    # Extract the problem name from the URL
    path = urlparse(url).path
    problem_name = os.path.basename(path)  # Extract the last part of the path
    return problem_name

def load_urls_from_file(file_path):
    # Read URLs from the file and strip whitespace characters like newlines
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def trim_text(text, prefix_marker, suffix_marker):
    # Trim text to remove everything before the prefix_marker and after the suffix_marker
    if prefix_marker in text:
        # Find the position of the prefix_marker and trim the text before it
        text = text.split(prefix_marker, 1)[1]
    if suffix_marker in text:
        # Find the position of the suffix_marker and trim the text after it
        text = text.split(suffix_marker, 1)[0]
    return text

def main():
    urls = load_urls_from_file(urls_file)

    # Define the strings to mark the start and end of the section we want to keep
    prefix_marker = "Statistici"  # Change to the string marking the start of the section
    suffix_marker = "Trebuie sa te autentifici pentru a trimite solutii."  # Change to the string marking the end of the section

    # Iterate over the list of URLs
    for i, url in enumerate(urls):
        print(f"Processing {url} ({i + 1}/{len(urls)})")

        # Step 1: Fetch the page content
        html_content = fetch_page_content(url)

        if html_content:
            # Step 2: Extract the text content from the HTML
            page_text = extract_text_from_html(html_content)

            # Step 3: Trim the text based on the markers
            trimmed_text = trim_text(page_text, prefix_marker, suffix_marker)

            # Step 4: Extract the problem name from the URL
            problem_name = get_problem_name_from_url(url)

            # Step 5: Save the trimmed text content to a file in the 'infoarena' directory
            page_filename = os.path.join(output_dir, f"{problem_name}.txt")
            save_text_to_file(trimmed_text, page_filename)
            print(f"Saved text to {page_filename}")
        else:
            print(f"Skipping {url} due to an error")


if __name__ == "__main__":
    main()
