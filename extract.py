import re

def extract_total(text):
    # Look for patterns like "Total : 9.00"
    match = re.search(r'total\s*[:\-]?\s*(\d+\.\d{2})', text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def extract_date(text):
    # Match date formats like 25/12/2018
    match = re.search(r'\b\d{2}/\d{2}/\d{4}\b', text)
    if match:
        return match.group(0)
    return None


def extract_company(text):
    # Assume company name is in first few lines
    lines = text.split('\n')
    for line in lines[:5]:
        if len(line.strip()) > 5:
            return line.strip()
    return None


def extract_all(text):
    return {
        "company": extract_company(text),
        "date": extract_date(text),
        "total": extract_total(text)
    }