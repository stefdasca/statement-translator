import requests
from bs4 import BeautifulSoup

# Function to scrape and process text
def scrape_and_process_text(url):
    # Step 1: Scrape the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 2: Extract main content (you may need to adjust this based on the webpage structure)
    main_content = soup.find('div', {'class': 'main-content'})  # Adjust to your website's structure
    if main_content is None:
        main_content = soup.body  # Fallback to body if no specific class is found

    # Step 3: Clean the text
    # Remove unwanted tags (e.g., script, style)
    for tag in main_content(['script', 'style', 'footer', 'header']):
        tag.extract()

    # Extract text and keep the structure intact
    text_lines = main_content.stripped_strings  # Extract strings and preserve line breaks

    # Step 4: Process and reformat the text
    processed_text = '\n\n'.join(text_lines)  # Reconstruct the text by adding line breaks between sections

    return processed_text

def load_urls_from_file(file_path):
    # Read URLs from the file and strip whitespace characters like newlines
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

urls_file = 'listproblems-monthly.txt'
urls = load_urls_from_file(urls_file)

# Define the strings to mark the start and end of the section we want to keep
prefix_marker = "Statistici"  # Change to the string marking the start of the section
suffix_marker = "Trebuie sa te autentifici pentru a trimite solutii."  # Change to the string marking the end of the section

# Iterate over the list of URLs
for i, url in enumerate(urls):
    print(f"Processing {url} ({i + 1}/{len(urls)})")
    formatted_text = scrape_and_process_text(url)

    print(formatted_text)
