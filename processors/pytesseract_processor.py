from .base import BaseProcessor
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
import tempfile

class PytesseractProcessor(BaseProcessor):
    name = "pytesseract"

    def process(self, pdf_path: Path) -> Path:
        out = self.output_dir /f"{pdf_path.stem}_{self.name}.txt"
        pages = convert_from_path(str(pdf_path))
        texts = []
        for page in pages:
            texts.append(pytesseract.image_to_string(page))
        out.write_text("\n".join(texts), encoding = "utf-8")
        return out