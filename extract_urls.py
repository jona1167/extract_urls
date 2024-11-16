import os
import re

# Function to extract URLs from a text file
def extract_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Regular expression to find URLs starting with http:// or https://
        urls = re.findall(r'(https?://[^\s]+)', content)
        return urls

# Function to process all .txt files in the current directory and save extracted URLs to done.txt
def process_files(directory):
    extracted_urls = []
    
    # Loop through all files in the provided directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            urls = extract_urls(file_path)
            extracted_urls.extend(urls)
    
    # Save all extracted URLs to done.txt, each URL on a new line
    with open(os.path.join(directory, 'done.txt'), 'w', encoding='utf-8') as output_file:
        for url in extracted_urls:
            output_file.write(url + '\n')

# Automatically detect the folder where the script (or exe) is located
current_directory = os.getcwd()
process_files(current_directory)

print("URLs have been extracted and saved to done.txt")