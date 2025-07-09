def find_missing_skills(user_skills, required_skills):
    missing = set(required_skills) - set(user_skills)
    return list(missing)
