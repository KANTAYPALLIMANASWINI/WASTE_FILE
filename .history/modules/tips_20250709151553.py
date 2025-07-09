import re

# ✅ Expected sections and keywords for a good resume
expected_sections = ['education', 'skills', 'experience', 'projects', 'career objective', 'certifications','contacts']
expected_keywords = ['python', 'java', 'ml', 'data', 'project', 'communication', 'teamwork', 'leadership']

# 🧹 Helper: Clean symbols/emojis/special characters
def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())  # Keep only words and spaces

# 🔍 Generate improvement tips
def generate_tips(resume_text):
    tips = []
    cleaned_text = clean_text(resume_text)

    # ✅ Check for missing important sections
    for section in expected_sections:
        if section.lower() not in cleaned_text:
            tips.append(f"📌 Consider adding a **{section.capitalize()}** section.")

    # ✅ Check how many important keywords are present
    keyword_count = sum([1 for word in expected_keywords if word in cleaned_text])
    if keyword_count < 5:
        tips.append("🧠 Add more technical and soft skills to improve keyword coverage.")

    # ✅ Specific content tips
    if 'project' not in cleaned_text:
        tips.append("💼 Mention at least 1 or 2 **projects** with outcomes and technologies.")

    if 'certification' not in cleaned_text:
        tips.append("🎓 Add relevant certifications or online courses to boost credibility.")

    # ✅ If everything looks good
    if not tips:
        tips.append("🌟 Your resume looks well-structured! Just polish formatting if needed.")

    return tips
