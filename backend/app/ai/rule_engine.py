from typing import Dict, List


def generate_rule_based_suggestions(
    sections: Dict,
    ats_analysis: Dict
) -> List[str]:

    suggestions = []

    # -----------------------------
    # Structure Suggestions
    # -----------------------------

    structure = ats_analysis["breakdown"]["structure"]

    for issue in structure["feedback"]:
        suggestions.append(issue)

    # -----------------------------
    # Skills Suggestions
    # -----------------------------

    skill_count = ats_analysis["breakdown"]["skills"]["skill_count"]

    if skill_count < 8:
        suggestions.append(
            "Include more relevant technical skills that match your target job."
        )

    # -----------------------------
    # Projects
    # -----------------------------

    project_words = ats_analysis["breakdown"]["projects"]["strong_words"]

    if len(project_words) < 5:
        suggestions.append(
            "Use stronger action verbs like 'Designed', 'Implemented', or 'Optimized'."
        )

    # -----------------------------
    # Readability
    # -----------------------------

    readability = ats_analysis["breakdown"]["readability"]

    if readability["word_count"] > 700:
        suggestions.append(
            "Your resume is slightly lengthy. Consider shortening weaker project descriptions."
        )

    elif readability["word_count"] < 250:
        suggestions.append(
            "Your resume is too short. Add more project or experience details."
        )

    # -----------------------------
    # Experience
    # -----------------------------

    if not sections.get("experience"):

        suggestions.append(
            "Include internships or practical experience if available."
        )

    return suggestions