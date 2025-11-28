#!/usr/bin/env python3
"""
CLI for running PDF → text processors.
"""

import argparse
from pathlib import Path

from processors.pypdf2_processor import PyPDF2Processor
from processors.pytesseract_processor import PytesseractProcessor
from processors.ocrmypdf_processor import OCRmyPDFProcessor
from processors.easyocr_processor import EasyOCRProcessor
from processors.textract_processor import TextractProcessor  # optional


def collect_pdfs(pdf_paths: list[str], directory: str | None) -> list[Path]:
    pdfs = []

    if directory:
        dir_path = Path(directory)
        if not dir_path.exists():
            raise ValueError(f"Directory does not exist: {directory}")
        pdfs.extend(sorted(dir_path.glob("*.pdf")))

    for p in pdf_paths:
        pp = Path(p)
        if not pp.exists():
            raise ValueError(f"File not found: {p}")
        if pp.suffix.lower() != ".pdf":
            raise ValueError(f"Not a PDF: {p}")
        pdfs.append(pp)

    return pdfs


def run_processors(pdfs: list[Path], output_root: Path, use_textract=False):
    output_root.mkdir(parents=True, exist_ok=True)

    processors = [
        PyPDF2Processor(output_root),
        #PytesseractProcessor(output_root),
        OCRmyPDFProcessor(output_root),
        EasyOCRProcessor(output_root)
    ]

    if use_textract:
        processors.append(TextractProcessor(output_root))

    for pdf in pdfs:
        print(f"\n📄 Processing: {pdf.name}")
        for p in processors:
            print(f" → Running {p.name} …", end="")
            try:
                out = p.process(pdf)
                print(f" OK  (output: {out})")
            except Exception as e:
                print(f" FAILED: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Run multiple OCR/Text Extraction processors on PDFs"
    )
    parser.add_argument(
        "--pdfs",
        nargs="*",
        help="List of PDF files to process",
    )
    parser.add_argument(
        "--dir",
        help="Directory containing PDF files"
    )
    parser.add_argument(
        "--output",
        default="outputs",
        help="Output directory for extracted text"
    )
    parser.add_argument(
        "--textract",
        action="store_true",
        help="Enable AWS Textract processor"
    )

    args = parser.parse_args()

    pdfs = collect_pdfs(args.pdfs or [], args.dir)
    if not pdfs:
        print("No PDFs found. Provide --pdfs or --dir.")
        return

    run_processors(pdfs, Path(args.output), use_textract=args.textract)


if __name__ == "__main__":
    main()
