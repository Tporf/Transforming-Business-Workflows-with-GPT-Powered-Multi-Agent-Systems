from .agent_utils import call_agent

def candidate_response_agent(features_evaluation, api_key):
    system_msg = (
        "You are a recruiter. Based on the evaluation of criteria (listed below):\n"
        f"{features_evaluation}\n"
        "If more than half of the criteria are satisfactory, write a welcoming message to the candidate and offer several interview questions.\n"
        "Otherwise, politely inform about disqualification."
    )
    return call_agent(api_key, system_msg, features_evaluation)
