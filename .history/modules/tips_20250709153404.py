# modules/tips.py

import re

# ✅ Expected sections and keywords for a good resume (excluding 'contact' from tip logic)
expected_sections = ['education', 'skills', 'experience', 'projects', 'career objective', 'certifications']
expected_keywords = ['python', 'java', 'ml', 'data', 'project', 'communication', 'teamwork', 'leadership']

def clean_text(text):
    # Lowercase + remove symbols like ':' , '-', '*', etc.
    return re.sub(r'[^a-z\s]', '', text.lower())

# 🔍 Generate improvement tips
def generate_tips(resume_text):
    tips = []
    cleaned_text = clean_text(resume_text)

    # Check for missing important sections (except contact)
    for section in expected_sections:
        section_cleaned = clean_text(section)
        if section_cleaned not in cleaned_text:
            tips.append(f"📌 Consider adding a **{section.capitalize()}** section.")

    # Check keyword presence
    keyword_count = sum(1 for word in expected_keywords if word in cleaned_text)
    if keyword_count < 5:
        tips.append("🧠 Add more technical and soft skills to improve keyword coverage.")

    # Additional suggestions
    if 'project' not in cleaned_text:
        tips.append("💼 Mention at least 1 or 2 **projects** with outcomes and technologies.")
    if 'certification' not in cleaned_text:
        tips.append("🎓 Add relevant certifications or online courses to boost credibility.")

    # All good?
    if not tips:
        tips.append("🌟 Your resume looks well-structured! Just polish formatting if needed.")

    return tips
