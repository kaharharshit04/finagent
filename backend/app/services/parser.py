import pandas as pd
import pdfplumber
import io


def parse_csv(file_bytes):
    return pd.read_csv(io.BytesIO(file_bytes))


def parse_excel(file_bytes):
    return pd.read_excel(io.BytesIO(file_bytes))


def parse_pdf(file_bytes):
    data = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    data.append({"description": line})

    return pd.DataFrame(data)


def parse_file(filename, file_bytes):
    if filename.endswith(".csv"):
        return parse_csv(file_bytes)

    elif filename.endswith(".xlsx"):
        return parse_excel(file_bytes)

    elif filename.endswith(".pdf"):
        return parse_pdf(file_bytes)

    else:
        raise ValueError("Unsupported file format")