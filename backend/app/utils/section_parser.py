SECTION_HEADERS = {
    "summary": ["summary", "profile"],
    "skills": ["skills", "technical skills", "tech stack"],
    "projects": ["projects", "personal projects"],
    "experience": ["experience", "work experience"],
    "education": ["education"],
    "certifications": ["certifications", "certificates"]
}


def parse_resume_sections(text: str):

    sections = {}
    current_section = "other"

    sections[current_section] = []

    lines = text.split("\n")

    for line in lines:

        clean_line = line.strip().lower()

        found_section = None

        for section, keywords in SECTION_HEADERS.items():

            for keyword in keywords:

                if clean_line.startswith(keyword) and len(clean_line.split()) <= 4:
                    found_section = section
                    break

            if found_section:
                break

        if found_section:

            current_section = found_section

            if current_section not in sections:
                sections[current_section] = []

        else:
            sections[current_section].append(line)

    # Convert lists to strings
    for section in sections:
        sections[section] = "\n".join(sections[section]).strip()

    return sections