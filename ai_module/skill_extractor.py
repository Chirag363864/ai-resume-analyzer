import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "javascript", "react", "node",
    "machine learning", "deep learning", "tensorflow",
    "nlp", "mongodb", "sql", "html", "css"
]

def extract_skills(text):
    text = text.lower()
    doc = nlp(text)

    found_skills = set()

    # ✅ Check full text (handles multi-word skills)
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)