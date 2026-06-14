import re


def clean_resume_text(text: str) -> str:

    # Normalize line endings
    text = text.replace("\r", "\n")

    # Remove excessive spaces but preserve line structure
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove excessive blank lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()