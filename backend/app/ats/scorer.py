def calculate_ats_score(sections):

    score = 0

    strengths = []
    weaknesses = []

    # Required sections
    required_sections = [
        "skills",
        "projects",
        "education"
    ]

    # Check required sections
    for section in required_sections:

        if sections.get(section):

            score += 20
            strengths.append(f"{section.title()} section found")

        else:
            weaknesses.append(f"Missing {section} section")

    # Experience bonus
    if sections.get("experience"):

        score += 15
        strengths.append("Experience section present")

    # Certifications bonus
    if sections.get("certifications"):

        score += 10
        strengths.append("Certifications included")

    # Prevent score > 100
    score = min(score, 100)

    return {
        "ats_score": score,
        "strengths": strengths,
        "weaknesses": weaknesses
    }