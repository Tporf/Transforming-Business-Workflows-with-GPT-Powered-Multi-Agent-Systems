from .agent_utils import call_agent

def interview_scheduler_agent(resume_text, api_key):
    system_msg = (
        "You are an interview coordinator and job vacancy specialist.\n"
        "Based on the resume, suggest 3 available time slots for an interview.\n"
        "Also, provide a list of 3 vacancies that could be suitable for the candidate."
    )
    return call_agent(api_key, system_msg, resume_text)
