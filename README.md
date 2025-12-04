# CS410-Course-Project

To run this program, you need a PDF version of a resume. A sample resume is already included in the project so you can test it right away.
1. Open a terminal and make sure you have the PyPDF2 package installed. (You can install it using pip install PyPDF2 if needed.)
2. In the terminal, run: python src/main.py
3. The program will ask you to paste a link to a job posting. After you enter it, the software will scrape the text from that page and look for skill requirements. Note: Some job sites block scraping—Indeed is one example. Sites like Dice usually work well and allow the tool to extract job content correctly.
4. Once the posting is processed, the program will compare the job’s required skills with the resume and show you which skills are missing.
This lets you quickly see what areas you may need to learn or improve to match the job better.



This software is a Python program made of several small files that work together to compare a resume with job postings and find what skills the person is missing. First, it reads the text from a resume and a job posting, cleans it up, and breaks it into useful words using spaCy, a language processing tool. It then checks these words against a list of known skills stored in a JSON file. The software also uses TF-IDF to see which words in the job posting seem most important. After that, it looks at which skills the resume does not have, and gives each missing skill a score based on how often it appears in the job posting and whether it was marked as important. The main program brings all these steps together—scraping the job page, finding skills, comparing them, ranking them, and printing the results. The data folder provides example files, including a skill list and a sample resume used for testing.
