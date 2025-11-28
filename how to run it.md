# Install Stuff

## GhostScript
Download the Ghostscript installer from https://www.ghostscript.com/download/gsdnld.html

## Tesseract
Download the Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
Run the installer on your system - use the default path C:\Program Files\Tesseract-OCR

## Poppler
Instruction for windows:<br>
Go to: https://github.com/oschwartz10612/poppler-windows/releases/ <br>
Download the latest release (look for poppler-xx.xx.x_windows-x64.zip)<br>
Extract the ZIP file to a folder (e.g., C:\poppler) <br>
Add Poppler to your system PATH
Restart computer if required

# Running with CLI
In the project folder run the CLI:

1. Run on individual PDFs:<br>
   `python cli.py --pdfs input/pdf1.pdf input/pdf2.pdf`<br>

2. Run on a folder:<br>
   `python cli.py --dir input_pdfs/`<br>

3. Choose output directory:<br>
   `python cli.py --dir input_pdfs/ --output results/`<br>

4. Enable Textract:<br>
   `python cli.py --pdfs input.pdf --textract`
