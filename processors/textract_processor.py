import boto3
from pathlib import Path
from .base import BaseProcessor


class TextractProcessor(BaseProcessor):
    """
    Uses AWS Textract synchronous DetectDocumentText().
    Works best for image PDFs or single-page documents.
    """

    name = "textract"

    def __init__(self, output_dir: Path, region_name="eu-west-1"):
        super().__init__(output_dir)
        self.client = boto3.client("textract", region_name=region_name)

    def process(self, pdf_path: Path) -> Path:
        out_path = self.output_dir / f"{pdf_path.stem}_{self.name}.txt"

        with open(pdf_path, "rb") as f:
            data = f.read()

        # synchronous OCR call
        response = self.client.detect_document_text(
            Document={"Bytes": data}
        )

        lines = []
        for block in response.get("Blocks", []):
            if block.get("BlockType") == "LINE":
                lines.append(block["Text"])

        out_path.write_text("\n".join(lines), encoding="utf-8")
        return out_path
