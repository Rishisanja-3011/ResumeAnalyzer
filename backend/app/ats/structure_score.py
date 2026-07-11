def analyze_structure(sections):

    score = 0
    feedback = []


    weights = {
        "skills": 20,
        "projects": 20,
        "education": 15,
        "experience": 15,
        "certifications": 10,
    }


    for section, points in weights.items():

        if sections.get(section):

            score += points

        else:

            feedback.append(
                f"{section.title()} section missing"
            )


    return {
        "score": score,
        "feedback": feedback
    }    