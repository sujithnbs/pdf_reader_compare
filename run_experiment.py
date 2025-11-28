from pathlib import Path
from processors.pypdf2_processor import PyPDF2Processor
from processors.pytesseract_processor import PytesseractProcessor
from processors.ocrmypdf_processor import OCRmyPDFProcessor
from processors.easyocr_processor import EasyOCRProcessor
# import others...

def run(pdf_paths, output_root="outputs"):
    processors = [
        PyPDF2Processor(output_root),
        PytesseractProcessor(output_root),
        OCRmyPDFProcessor(output_root),
        EasyOCRProcessor(output_root),
    ]
    for pdf in pdf_paths:
        for p in processors:
            try:
                p.process(pdf)
            except Exception as e:
                print(f"Error in {p.name} for {pdf}: {e}")
#

## python run_experiment.py samples/