# gpt_api.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    prompt = f"""
            Summarize the following content into exactly three clearly separated bullet points using this format:
            Give the title head of the web page is about.
            Give a small summary of the entire page in 1 line to breifly explain what the context about the page is about.

            -Then, summarize the main ideas of the page in 3 bullet points using the below format:
            ⦿  Summary of the first point.

            ⦿  Summary of the second point.

            ⦿  Summary of the third point.

            Each bullet should cover a unique aspect and be concise (1-2 lines max). Don't merge all into one line.

            Content:
            {text}
    """


    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {str(e)}"
