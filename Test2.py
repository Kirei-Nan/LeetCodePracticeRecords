#pip install requests beautifulsoup4 pandas PyPDF2
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from PyPDF2 import PdfFileReader


# Define the function to get the chemical name based on CAS number
def get_chemical_name(cas_number):
    print(f"Fetching chemical name for CAS number: {cas_number}")
    url = f"https://www.chemicalbook.com/Search.aspx?keyword={cas_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the element that contains the English name based on the provided structure
        table_rows = soup.find_all('tr')
        for row in table_rows:
            cells = row.find_all('td')
            if len(cells) > 1 and "英文名称：" in cells[0].text:
                english_name_element = cells[1].find('a', class_='blue')
                if english_name_element:
                    english_name = english_name_element.text.strip()
                    print(f"Found chemical name: {english_name}")
                    return english_name
        print("English name not found")
        return "English name not found"
    else:
        print("Failed to retrieve data")
        return "Failed to retrieve data"


# Define the function to classify the clay type
def classify_clay_type(english_name):
    clay_types = [
        "Bentonite", "Montmorillonite", "Smectite", "Phyllosilicates",
        "Hectorite", "Sepiolite", "Attapulgite", "Fuller's earth", "Palygorskite"
    ]
    for clay_type in clay_types:
        if clay_type.lower() in english_name.lower():
            print(f"Classified as clay type: {clay_type}")
            return clay_type
    print("Clay type not found")
    return "not found"


# Define the function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = ''
        for page_num in range(reader.getNumPages()):
            text += reader.getPage(page_num).extract_text()
    return text


# Define the function to classify the clay type from PDF content
def classify_from_pdf(text):
    clay_types = [
        "Bentonite", "Montmorillonite", "Smectite", "Phyllosilicates",
        "Hectorite", "Sepiolite", "Attapulgite", "Fuller's earth", "Palygorskite"
    ]
    for clay_type in clay_types:
        if re.search(clay_type, text, re.IGNORECASE):
            print(f"Classified as clay type from PDF: {clay_type}")
            return clay_type
    return "not found"


# Load the uploaded Excel file
file_path = '/Users/nanzhenghan/Downloads/Data.xlsx'
data = pd.read_excel(file_path)

# Directory containing the TDS PDFs
pdf_directory = '/path/to/your/pdf/directory'


# Add a new column for Clay Type
def process_row(row):
    cas_number = row['CAS']
    champcode = row['champcode']

    clay_type = classify_clay_type(get_chemical_name(cas_number))

    if clay_type == "not found":
        pdf_path = os.path.join(pdf_directory, f"{champcode}.pdf")
        if os.path.exists(pdf_path):
            pdf_text = extract_text_from_pdf(pdf_path)
            clay_type = classify_from_pdf(pdf_text)

    return clay_type


data['Clay Type'] = data.apply(process_row, axis=1)

# Save the updated dataframe to a new Excel file
output_file_path = '/Users/nanzhenghan/Downloads/Updated_Data.xlsx'
data.to_excel(output_file_path, index=False)

print(f"Updated data saved to: {output_file_path}")