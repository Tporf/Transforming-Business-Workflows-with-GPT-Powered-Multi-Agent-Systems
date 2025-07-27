from openai import OpenAI

def create_openai_client(api_key):
    return OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

def call_agent(api_key, system_msg, user_msg, model="gemini-2.5-flash"):
    client = create_openai_client(api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ]
    )
    return response.choices[0].message.content
