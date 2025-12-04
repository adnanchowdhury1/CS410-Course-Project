from PyPDF2 import PdfReader
import requests
from bs4 import BeautifulSoup
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def scrape_job_posting(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    selectors = [
        {"id": "jobDescriptionText"},
        {"class": "jobsearch-jobDescriptionText"},
        {"class": "jobsearch-JobComponent-description"},
        {"class": "job-description"},
        {"class": "description"},
        {"class": "jobDescription"},
    ]

    for sel in selectors:
        results = soup.find_all(attrs=sel)
        if results:
            text = " ".join([r.get_text(separator=" ") for r in results])
            if len(text.strip()) > 100:
                return text

    return soup.get_text(separator=" ")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+\-. ]", " ", text)
    return text

def preprocess_text(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
