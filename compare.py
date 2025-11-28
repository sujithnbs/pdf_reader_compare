# compare.py
from pathlib import Path
from processors.pypdf2_processor import PyPDF2Processor
from processors.pytesseract_processor import PytesseractProcessor
from processors.easyocr_processor import EasyOCRProcessor
from processors.ocrmypdf_processor import OCRmyPDFProcessor
from processors.textract_processor import TextractProcessor


def compare_pdfs(pdf_paths, output_root="outputs"):
    """
    Runs all processor classes on each PDF and prints a comparison summary.
    """
    output_root = Path(output_root)

    processors = [
        PyPDF2Processor(output_root),
        PytesseractProcessor(output_root),
        EasyOCRProcessor(output_root),
        OCRmyPDFProcessor(output_root),
        TextractProcessor(output_root),
    ]

    for pdf_path in pdf_paths:
        pdf_path = Path(pdf_path)
        print("=" * 80)
        print(f"Processing: {pdf_path.name}")
        print("=" * 80)

        for processor in processors:
            print(f"\n--- {processor.name.upper()} ---")
            try:
                out_file = processor.process(pdf_path)
                # Show short preview for comparison
                text = out_file.read_text(encoding="utf-8", errors="ignore")
                preview = text[:500].replace("\n", " ")
                print(f"Output saved: {out_file}")
                print(f"Preview: {preview}...")
            except Exception as e:
                print(f"❌ Error running {processor.name}: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python compare.py file1.pdf file2.pdf ...")
        exit(1)

    compare_pdfs(sys.argv[1:])
