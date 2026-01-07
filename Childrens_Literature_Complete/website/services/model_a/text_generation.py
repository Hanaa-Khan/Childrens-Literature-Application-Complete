import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() 

## client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)

def generate_story_a(prompt: str) -> str:
    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}  
        ]
    )
    story = response.choices[0].message.content
    print("Generated story:", story[:100])
    return story