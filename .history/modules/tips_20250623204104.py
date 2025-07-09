# modules/tips.py

# ✅ Expected sections and keywords for a good resume
expected_sections = [ 'education', 'skills', 'experience', 'projects','objective', 'certifications', 'contact']
expected_keywords = ['python', 'java', 'ml', 'data', 'project', 'communication', 'teamwork', 'leadership']

# 🔍 Generate improvement tips
def generate_tips(resume_text):
    tips = []

    # Check for missing important sections
    for section in expected_sections:
        if section not in resume_text.lower():
            tips.append(f"📌 Consider adding a **{section.capitalize()}** section.")

    # Check how many important keywords are present
    keyword_count = sum([1 for word in expected_keywords if word in resume_text.lower()])
    if keyword_count < 5:
        tips.append("🧠 Add more technical and soft skills to improve keyword coverage.")

    # Specific content tips
    if 'project' not in resume_text.lower():
        tips.append("💼 Mention at least 1 or 2 **projects** with outcomes and technologies.")

    if 'certification' not in resume_text.lower():
        tips.append("🎓 Add relevant certifications or online courses to boost credibility.")

    # If everything looks good
    if not tips:
        tips.append("🌟 Your resume looks well-structured! Just polish formatting if needed.")

    return tips
