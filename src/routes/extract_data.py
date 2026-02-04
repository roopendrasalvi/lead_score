from fastapi import APIRouter
from src.utils.extract_data import file_to_text

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
@router.post("/extract-data")
def extract_data(
    file_path: str
):
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash')
    full_text = file_to_text(file_path)
    requirement = file_to_text(os.getenv("REQUIREMENT_PATH"))

    prompt = f"""
You are an expert candidate fit scoring analyst.
Evaluate how well the skills and experiences extracted from a candidate's resume 
align with the requirements listed for a specific job role.

Resume data (extracted): {full_text}

Job requirements (from database): {requirement}

Instructions:
- Check if each resume skill/experience directly matches or closely relates to any requirement.
- Consider synonyms and equivalent terms (e.g., "JS" vs "JavaScript", "ML" vs "Machine Learning").
- If a skill or experience is not in the requirements list, mark it as a mismatch.
- Base your scoring only on the provided requirements list.

Output format:
"Based on requirement alignment, this candidate has a [X]% fit for the role.
Key factors:
- [bullet point 1]
- [bullet point 2]"
"""

    response = model.generate_content(prompt)
    response_data = {
        "response": response.text
    }
    return response_data