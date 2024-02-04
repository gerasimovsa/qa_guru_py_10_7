import os.path


ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(ROOT, "data")
RESOURCES = os.path.join(ROOT, "resources")

DATA_FILES = os.listdir(DATA)

ARCHIVE = os.path.join(RESOURCES, "sample_zip.zip")
EXTRACTED_CSV = os.path.join(RESOURCES, "csv_sample.csv")
EXTRACTED_PDF = os.path.join(RESOURCES, "pdf_sample.pdf")
EXTRACTED_XLSX = os.path.join(RESOURCES, "xlsx_sample.xlsx")
