import random
from dotenv import load_dotenv
import os

from agents.resume_evaluator import resume_evaluator_agent
from agents.candidate_response import candidate_response_agent
from agents.interview_scheduler import interview_scheduler_agent

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Пример резюме — можно подгружать из файла data/sample_resumes.txt
resumes = [
    "Work experience: 3 years in Python development. Skills: Django, Flask, SQL. Education: higher technical.",
    "Work experience: 1 year in customer support. Skills: communication, CRM. Education: specialized secondary.",
    "Work experience: 5 years in marketing. Skills: SEO, content marketing, analytics. Education: higher economics."
]

resume = random.choice(resumes)
print("Resume to evaluate:\n", resume, "\n")

features = resume_evaluator_agent(resume, api_key=API_KEY)
print("Criteria evaluation:\n", features, "\n")

response_to_candidate = candidate_response_agent(features, api_key=API_KEY)
print("Response to candidate:\n", response_to_candidate, "\n")

if features.count("satisfactory") > features.count("unsatisfactory"):
    interview_info = interview_scheduler_agent(resume, api_key=API_KEY)
    print("Interview and vacancies information:\n", interview_info)
else:
    print("Candidate did not pass preliminary screening. Interview is not scheduled.")
