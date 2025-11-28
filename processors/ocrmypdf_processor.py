import os
os.environ['PATH'] = r'C:\Program Files\gs\gs10.00\bin' + os.pathsep + os.environ['PATH']

import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from .base import BaseProcessor
import subprocess
from pathlib import Path
import tempfile


import warnings
warnings.filterwarnings('ignore', message='.*pin_memory.*')

class OCRmyPDFProcessor(BaseProcessor):
    name = 'ocrmypdf'

    def process(self, pdf_path: Path) -> Path:
        ocr_pdf = self.output_dir /f"{pdf_path.stem}.pdf"
        txt_out = self.output_dir /f"{pdf_path.stem}_{self.name}.txt"

        cmd = [
            "ocrmypdf",
            #"-l", "eng",
            "--skip-text",
            str(pdf_path),
            str(ocr_pdf),
        ]

        #subprocess.run(cmd, check=True)
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            print(f"Return code: {result.returncode}")

        # now extract text from ocr_pdf using pdf2text or PyPDF2
        # for simplicity use pdftotext (from poppler)
        subprocess.run(["pdftotext", "-layout", str(ocr_pdf), str(txt_out.with_suffix(".txt"))], check=True)
        return txt_out.with_suffix(".txt")