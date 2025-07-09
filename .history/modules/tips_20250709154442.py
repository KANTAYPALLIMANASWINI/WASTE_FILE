import re

# ✅ Expected sections and keywords (excluding 'contact')
expected_sections = []
expected_keywords = ['python', 'java', 'ml', 'data', 'project', 'communication', 'teamwork', 'leadership']

# 🔧 Clean text to remove symbols
def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

# 💡 Generate improvement tips
def generate_tips(resume_text):
    tips = []
    cleaned_text = clean_text(resume_text)

    # 🔍 Section presence check
    for section in expected_sections:
        pattern = r'\b' + re.escape(section.lower()) + r'\b'
        if not re.search(pattern, cleaned_text):
            tips.append(f"📌 Consider adding a **{section.capitalize()}** section.")

    # 🔍 Keyword richness
    keyword_count = sum(1 for keyword in expected_keywords if re.search(r'\b' + keyword + r'\b', cleaned_text))
    if keyword_count < 5:
        tips.append("🧠 Add more technical and soft skills to improve keyword coverage.")

    # 💼 Specific additions
    if not re.search(r'\bproject\b', cleaned_text):
        tips.append("💼 Mention at least 1 or 2 **projects** with outcomes and technologies.")

    if not re.search(r'\bcertification\b', cleaned_text):
        tips.append("🎓 Add relevant certifications or online courses to boost credibility.")

    # ✅ Looks good?
    if not tips:
        tips.append("🌟 Your resume looks well-structured! Just polish formatting if needed.")

    return tips
