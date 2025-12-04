from preprocess import read_pdf, scrape_job_posting, clean_text, preprocess_text
from extract_skills import load_skill_dictionary, extract_skills_from_tokens, tfidf_keywords
from rank_skills import rank_missing_skills

def main():
    print("===== Resume Gap Finder =====")
    url = input("Paste job posting URL: ")

    resume_text = read_pdf("data/sample-resume.pdf")
    resume_clean = clean_text(resume_text)
    resume_tokens = preprocess_text(resume_clean)

    print("Scraping job posting...")
    job_raw = scrape_job_posting(url)
    job_clean = clean_text(job_raw)
    job_tokens = preprocess_text(job_clean)

    skill_dict = load_skill_dictionary()

    resume_skills = extract_skills_from_tokens(resume_tokens, skill_dict)
    job_skills = extract_skills_from_tokens(job_tokens, skill_dict)

    job_tfidf = tfidf_keywords(job_clean)

    job_freq = {skill: job_tokens.count(skill) for skill in job_skills}
    missing = list(set(job_skills) - set(resume_skills))

    ranked = rank_missing_skills(missing, job_freq, job_tfidf)

    print("\n===== Missing Skills (Ranked) =====")
    for skill, score in ranked:
        print(f"{skill}: {score}")

if __name__ == "__main__":
    main()
