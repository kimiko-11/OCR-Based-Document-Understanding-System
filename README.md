OCR-Based Document Understanding System
Overview

This project implements an end-to-end pipeline to extract structured information from receipt images using computer vision and OCR techniques.

Features
Image preprocessing (grayscale, noise removal, thresholding, deskewing)
Text extraction using Tesseract OCR
Word-level bounding box detection
Key information extraction (company, date, total)
Structured JSON output
Pipeline

Input Image → Preprocessing → OCR → Bounding Boxes → Information Extraction → JSON Output

Project Structure
preprocessing.py
ocr.py
extract.py
main.py
data/
outputs/
Installation
pip install -r requirements.txt

Install Tesseract OCR and ensure it is added to PATH.

Usage
python main.py
Output
Image with detected text bounding boxes
Extracted structured data in JSON format
Tech Stack

Python, OpenCV, Tesseract OCR, NumPy, Matplotlib

Author

Kimaya Chavan
