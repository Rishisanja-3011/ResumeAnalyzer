from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_resume_text
from app.utils.section_parser import parse_resume_sections
from app.ats.scorer import calculate_ats_score

from app.ai.rule_engine import generate_rule_based_suggestions
from app.ai.prompt_builder import build_resume_analysis_prompt

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

# ATS Analysis
    ats_results = calculate_ats_score(
    parsed_sections,
    cleaned_text
)

# Rule-Based Suggestions
    rule_suggestions = generate_rule_based_suggestions(
    parsed_sections,
    ats_results
)
    prompt = build_resume_analysis_prompt(
    parsed_sections,
    ats_results,
    rule_suggestions
)

    return {
        "filename": file.filename,
        "sections": parsed_sections,
        "ats_analysis":ats_results,
        "rule_suggestions": rule_suggestions,
        "prompt": prompt
    }