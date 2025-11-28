import easyocr
from .base import BaseProcessor
from pathlib import Path
from pdf2image import convert_from_path
import numpy as np

class EasyOCRProcessor(BaseProcessor):
    name = 'easyocr'
    reader = easyocr.Reader(['en'], gpu=True) # set to false if GPU not available

    def process(self, pdf_path:Path)-> Path:
        out = self.output_dir / f"{pdf_path.stem}_{self.name}.txt"
        pages = convert_from_path(str(pdf_path))
        texts = []
        for page in pages:
            img = page
            result = self.reader.readtext(np.array(img))
            # result -> list of (bbox, text, confidence)
            texts.append(" ".join([r[1] for r in result]))
        out.write_text("\n\n".join(texts), encodings = "utf-8")
        return out
    