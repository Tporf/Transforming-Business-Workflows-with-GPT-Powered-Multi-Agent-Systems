from .agent_utils import call_agent

def resume_evaluator_agent(resume_text, api_key):
    system_msg = (
        "You are an HR analyst. Evaluate the resume based on the following criteria:\n"
        "- Experience relevance to the job opening\n"
        "- Presence of key skills\n"
        "- Level of education\n"
        "Output the list of criteria with evaluation 'satisfactory' or 'unsatisfactory'."
    )
    return call_agent(api_key, system_msg, resume_text)
