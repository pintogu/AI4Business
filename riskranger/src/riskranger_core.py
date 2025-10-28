import fitz  # PyMuPDF
from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator

DetectorFactory.seed = 0  # reproducible language detection

def read_pdf_bytes(pdf_bytes, filename="uploaded.pdf"):
    """Return list of dicts {source, page, section, text} from a PDF file's bytes."""
    rows = []
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for i, page in enumerate(doc, start=1):
            text = page.get_text("text").strip()
            if not text:
                continue
            rows.append({"source": filename, "page": i, "section": "", "text": text})
    return rows

def detect_lang_safe(text: str) -> str:
    try:
        return detect(text) if text and text.strip() else "unknown"
    except Exception:
        return "unknown"

def get_translator():
    # Uses GoogleTranslator via deep-translator (needs internet)
    return GoogleTranslator(source="auto", target="en")

def translate_to_en(text: str, translator=None):
    """Return (text_en, translated_flag)."""
    translator = translator or get_translator()
    if not text or not text.strip():
        return text, False
    try:
        return translator.translate(text), True
    except Exception:
        return text, False
