import re
import textract
import os

def extract_abbreviations(text):
    abbreviations = set()  # Use a set to automatically handle duplicates
    abbreviation_pattern = r'\(([A-Z]+)\)'
    matches = re.findall(abbreviation_pattern, text)
    for match in matches:
        abbreviations.add(match)
    return abbreviations

# Get the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_directory)

# Load text content from the .docx document using textract
document_content = textract.process("report.docx").decode('utf-8')

# Extract unique abbreviations from the document content
unique_abbreviations = extract_abbreviations(document_content)

# Sort the abbreviations alphabetically
sorted_abbreviations = sorted(unique_abbreviations)

# Print the sorted list of abbreviations
for index, abbreviation in enumerate(sorted_abbreviations, start=1):
    print(f"{index}. {abbreviation}")
