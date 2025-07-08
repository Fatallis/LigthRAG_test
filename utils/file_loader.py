# utils/file_loader.py
import os
import fitz  # PyMuPDF
from docx import Document

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_md(path):
    return read_txt(path)

def read_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def read_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

EXTENSIONS = {
    ".txt": read_txt,
    ".md": read_md,
    ".pdf": read_pdf,
    ".docx": read_docx
}

def load_documents_from_folder(folder):
    docs = []
    for filename in os.listdir(folder):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext in EXTENSIONS:
            path = os.path.join(folder, filename)
            try:
                text = EXTENSIONS[ext](path)
                cleaned = clean_text(text)
                chunks = chunk_text(cleaned)
                for i, chunk in enumerate(chunks):
                    docs.append(f"[{filename}] {chunk}")
            except Exception as e:
                print(f"❌ Error leyendo {filename}: {e}")
    return docs

def clean_text(text):
    return ' '.join(text.strip().split())

def chunk_text(text, max_length=500):
    sentences = text.split(". ")
    chunks = []
    current = ""
    for s in sentences:
        if len(current) + len(s) <= max_length:
            current += s + ". "
        else:
            chunks.append(current.strip())
            current = s + ". "
    if current:
        chunks.append(current.strip())
    return chunks
