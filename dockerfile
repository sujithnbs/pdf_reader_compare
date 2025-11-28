# Use an official slim Python base
FROM python:3.11-slim

# Install system packages needed for pdf -> image & OCR and building some Python deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    poppler-utils \            # pdftotext, pdf2image dependency
    tesseract-ocr \            # pytesseract backend
    libtesseract-dev \
    libjpeg-dev \
    zlib1g-dev \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements file (you will create this)
COPY requirements.txt .

# Install Python deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy the project
COPY . .

# Expose optional port if you run any local server (not strictly necessary)
EXPOSE 8080

# Default entrypoint - container will drop into shell unless overridden
ENTRYPOINT [ "bash", "-lc" ]
