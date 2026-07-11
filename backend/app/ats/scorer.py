from app.ats.structure_score import analyze_structure
from app.ats.skill_score import analyze_skills
from app.ats.project_score import analyze_projects
from app.ats.readability_score import analyze_readability



def calculate_ats_score(
        sections,
        full_text
):


    structure = analyze_structure(sections)

    skills = analyze_skills(sections)

    projects = analyze_projects(sections)

    readability = analyze_readability(full_text)



    final_score = (

        structure["score"] * 0.30 +

        skills["score"] * 0.25 +

        projects["score"] * 0.30 +

        readability["score"] * 0.15
    )


    return {


        "overall_score": round(final_score),


        "breakdown": {


            "structure": structure,

            "skills": skills,

            "projects": projects,

            "readability": readability
        }
    }