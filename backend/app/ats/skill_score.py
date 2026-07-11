TECH_SKILLS = [

    "python",
    "java",
    "javascript",

    "react",
    "node",
    "flask",
    "fastapi",

    "mysql",
    "postgresql",
    "mongodb",

    "docker",
    "git",

    "machine learning",
    "api"
]


def analyze_skills(sections):

    skills_text = sections.get(
        "skills",
        ""
    ).lower()


    detected = []


    for skill in TECH_SKILLS:

        if skill in skills_text:

            detected.append(skill)



    score = min(
        len(detected) * 5,
        100
    )


    return {

        "score": score,

        "detected_skills": detected,

        "skill_count": len(detected)
    }