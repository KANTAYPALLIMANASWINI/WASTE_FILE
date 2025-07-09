import os
import json
import pandas as pd
from pdfminer.high_level import extract_text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

skills_db = [
    'python', 'java', 'c', 'html', 'css', 'machine learning', 'data analysis',
    'communication', 'teamwork', 'javascript', 'react', 'django', 'sql',
    'excel', 'oops', 'dsa', 'problem solving', 'figma', 'adobe', 'creativity'
]

job_roles = {
    'Frontend Developer': ['html', 'css', 'javascript', 'react'],
    'Backend Developer': ['python', 'django', 'flask', 'sql'],
    'Data Analyst': ['python', 'excel', 'sql', 'data analysis'],
    'Machine Learning Engineer': ['python', 'ml', 'numpy', 'pandas'],
    'Full Stack Developer': ['html', 'css', 'javascript', 'python', 'django'],
    'Software Engineer': ['java', 'oops', 'dsa', 'problem solving'],
    'UI/UX Designer': ['figma', 'adobe', 'creativity'],
    'Communication Executive': ['communication', 'english', 'presentation']
}

expected_sections = ['objective', 'education', 'skills', 'experience', 'projects', 'certifications', 'contact']
expected_keywords = ['python', 'java', 'ml', 'data', 'project', 'communication', 'teamwork', 'leadership']

def build_resume(uploaded_file):
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text("temp_resume.pdf")

    words = word_tokenize(resume_text.lower())
    filtered_words = [w for w in words if w.isalnum() and w not in stopwords.words('english')]
    extracted_skills = list(set(filtered_words) & set(skills_db))

    best_match = None
    max_match_count = 0
    for role, required_skills in job_roles.items():
        match_count = len(set(extracted_skills) & set(required_skills))
        if match_count > max_match_count:
            max_match_count = match_count
            best_match = role

    section_score = sum([1 for section in expected_sections if section in resume_text.lower()])
    keyword_score = sum([1 for word in expected_keywords if word in resume_text.lower()])
    total_score = section_score + keyword_score
    resume_rating = round((total_score / 15) * 10, 1)

    result = {
        "Extracted Skills": extracted_skills,
        "Predicted Job Role": best_match if best_match else "No suitable role found",
        "Resume Rating (out of 10)": resume_rating
    }

    return result
