import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(question, context):
    prompt = f"""
You are an AI Resume Analyzer.

Use ONLY the resume information below.

Resume:

{context}

Question:
{question}

Answer clearly.
"""

    response = model.generate_content(prompt)

    return response.text