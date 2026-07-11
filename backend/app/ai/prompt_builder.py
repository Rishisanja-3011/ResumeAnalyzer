from typing import Dict, List


def build_resume_analysis_prompt(
    sections: Dict,
    ats_analysis: Dict,
    rule_suggestions: List[str]
) -> str:

    prompt = f"""
You are an expert ATS recruiter, career coach, and resume reviewer.

Analyze the following resume information.

==========================
RESUME SECTIONS
==========================

Summary:
{sections.get("summary", "")}

Experience:
{sections.get("experience", "")}

Skills:
{sections.get("skills", "")}

Projects:
{sections.get("projects", "")}

Education:
{sections.get("education", "")}

Certifications:
{sections.get("certifications", "")}

==========================
ATS ANALYSIS
==========================

Overall ATS Score:
{ats_analysis["overall_score"]}

ATS Breakdown:
{ats_analysis["breakdown"]}

==========================
RULE-BASED SUGGESTIONS
==========================

{chr(10).join(rule_suggestions)}

==========================
TASK
==========================

Based on the resume and ATS analysis:

1. Identify the top 5 improvements.
2. Explain WHY each improvement matters.
3. Rewrite weak resume statements if needed.
4. Suggest missing ATS keywords.
5. Keep suggestions specific and actionable.
6. Do NOT invent fake experience.
7. Respond in clean markdown.
"""

    return prompt