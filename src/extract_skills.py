import json
from sklearn.feature_extraction.text import TfidfVectorizer

def load_skill_dictionary(path="data/skills.json"):
    with open(path, "r") as f:
        return json.load(f)

def extract_skills_from_tokens(tokens, skill_dict):
    return [skill for skill in skill_dict if skill in tokens]

def tfidf_keywords(job_text, top_k=20):
    vec = TfidfVectorizer(stop_words="english")
    tfidf = vec.fit_transform([job_text])
    feature_names = vec.get_feature_names_out()
    scores = tfidf.toarray()[0]

    top_idx = scores.argsort()[-top_k:]
    return [feature_names[i] for i in top_idx]
