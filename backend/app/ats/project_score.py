QUALITY_TERMS = [

    "built",
    "developed",
    "implemented",
    "designed",
    "optimized",
    "integrated",
    "deployed",
    "automated"
]


def analyze_projects(sections):


    projects = sections.get(
        "projects",
        ""
    ).lower()


    matches = []


    for term in QUALITY_TERMS:

        if term in projects:

            matches.append(term)



    score = min(
        len(matches) * 15,
        100
    )


    return {

        "score": score,

        "strong_words": matches
    }