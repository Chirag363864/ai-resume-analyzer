best_role = ""
best_match = 0

for role, role_skills in job_roles.items():
    match = len(set(skills).intersection(role_skills))

    if match > best_match:
        best_match = match
        best_role = role

score = min(100, best_match * 25)

suggestions = []

if score < 50:
    suggestions.append("Add more relevant technical skills")

if "projects" not in text.lower():
    suggestions.append("Include project experience")

if "education" not in text.lower():
    suggestions.append("Add education section")

result = {
    "skills": skills,
    "job_role": best_role,
    "score": score,
    "suggestions": suggestions
}