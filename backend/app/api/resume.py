from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.ats.scorer import calculate_ats_score

from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.utils.section_parser import parse_resume_sections

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Clean text
    cleaned_text = clean_resume_text(extracted_text)

    # Parse sections
    parsed_sections = parse_resume_sections(cleaned_text)
    ats_results = calculate_ats_score(
    parsed_sections,
    cleaned_text
)

    return {
        "filename": file.filename,
        "sections": parsed_sections,
        "ats_analysis":ats_results
    }