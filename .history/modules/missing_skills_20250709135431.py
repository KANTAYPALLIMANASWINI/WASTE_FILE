# ✅ missing_skills.py

# Predefined job role skill requirements
job_skills = {
    'Frontend Developer': ['html', 'css', 'javascript', 'react'],
    'Backend Developer': ['python', 'django', 'sql'],
    'Data Analyst': ['python', 'excel', 'sql', 'data analysis'],
    'Machine Learning Engineer': ['python', 'ml', 'numpy', 'pandas'],
    'Full Stack Developer': ['html', 'css', 'javascript', 'python', 'django'],
    'Software Engineer': ['java', 'oops', 'dsa'],
    'UI/UX Designer': ['figma', 'adobe', 'creativity'],
    'Communication Executive': ['communication', 'english', 'presentation']
    
}

# Learning links
learning_links = {
    'python': 'https://www.learnpython.org/',
    'html': 'https://developer.mozilla.org/en-US/docs/Web/HTML',
    'css': 'https://developer.mozilla.org/en-US/docs/Web/CSS',
    'javascript': 'https://www.javascript.info/',
    'react': 'https://react.dev/learn',
    'django': 'https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django',
    'sql': 'https://www.codecademy.com/learn/learn-sql',
    'excel': 'https://exceljet.net/',
    'java': 'https://www.w3schools.com/java/',
    'oops': 'https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/',
    'dsa': 'https://www.geeksforgeeks.org/data-structures/',
    'communication': 'https://www.coursera.org/learn/wharton-communication',
    'teamwork': 'https://www.edx.org/course/teamwork-skills-communicating-effectively-in-groups',
    'data analysis': 'https://www.coursera.org/specializations/data-analysis',
    'ml': 'https://developers.google.com/machine-learning/crash-course',
    'numpy': 'https://numpy.org/learn/',
    'pandas': 'https://pandas.pydata.org/docs/getting_started/index.html'
}

# 🔍 Step 1: Find missing skills based on role
def find_missing_skills(user_skills, predicted_role):
    required = job_skills.get(predicted_role, [])
    missing = list(set(required) - set(user_skills))
    return missing

# 📚 Step 2: Get learning links for the missing ones
def get_learning_links(skills):
    links = {}
    for skill in skills:
        links[skill] = learning_links.get(skill.lower(), '🔍 Link not found')
    return links
