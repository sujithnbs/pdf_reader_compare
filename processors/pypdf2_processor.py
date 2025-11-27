from .base import BaseProcessor
from pathlib import Path
import PyPDF2

class PyPDF2Processor(BaseProcessor):
    name = 'pypdf2'

    def process(self, pdf_path: Path) -> Path:
        out = self.output_dir/ f"{pdf_path.stem}_(self.name).txt"
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            texts = []
            for page in reader.pages:
                texts.append(page.extractText() or "")

        text = "\n".join(texts)
        out.write_text(text, encodings = "utf-8")
        return out
