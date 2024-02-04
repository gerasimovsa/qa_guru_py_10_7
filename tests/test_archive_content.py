from openpyxl import load_workbook
from pypdf import PdfReader
import csv
from zipfile import ZipFile
from utils.paths import *


def test_csv_content():
    with ZipFile(ARCHIVE, "r") as extractor:
        extractor.extract("csv_sample.csv", RESOURCES)
    with open(EXTRACTED_CSV, "r", encoding="UTF-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        row = next(csv_reader)
        assert row == ['ID07351', '1-янв.', 'East', 'Boston', 'Bars', 'Carrot', '33', '1,77', '58,41']


def test_pdf_content():
    with ZipFile(ARCHIVE, "r") as extractor:
        extractor.extract("pdf_sample.pdf", RESOURCES)
    pdf_reader = PdfReader(EXTRACTED_PDF)
    text = pdf_reader.pages[30].extract_text().split('\n')[0].lstrip()
    assert text == "All Engines Go – The Basics of Game QA 14"


def test_xlsx_content():
    with ZipFile(ARCHIVE, "r") as extractor:
        extractor.extract("xlsx_sample.xlsx", RESOURCES)
    workbook = load_workbook(EXTRACTED_XLSX)
    sheet = workbook.active
    assert sheet[5][3].value == "New York"
    assert sheet[5][4].value == "Cookies"
    assert sheet[5][5].value == "Chocolate Chip"

