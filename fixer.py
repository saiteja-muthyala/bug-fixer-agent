from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def fix_code(code: str, error: str) -> str:
    prompt = f"""
You are a Python debugging expert. Given the following code and error message, identify the bug and suggest a corrected version of the code with explanations.

Code:
{code}

Error Message:
{error}

Respond in this format:
1. Issue Summary
2. Suggested Fix
3. Corrected Code
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
