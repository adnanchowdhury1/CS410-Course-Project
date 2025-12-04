def rank_missing_skills(missing_skills, job_skill_freq, tfidf_list):
    ranked = []

    for skill in missing_skills:
        score = 0

        score += job_skill_freq.get(skill, 0)

        if skill in tfidf_list:
            score += 1.5

        ranked.append((skill, score))

    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked
