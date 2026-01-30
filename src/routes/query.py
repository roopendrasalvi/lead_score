from fastapi import APIRouter, HTTPException
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

from src.database.get_db import get_db

# with open("config/prompt.yaml", "r") as file:
#     data = yaml.safe_load(file)

router = APIRouter()

def clean_df(df):
    menu_items = df["Item"].tolist()
    return menu_items

@router.post("/query")
def query(
    query: str
):
    
    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash')
        
    interests = query

    df = get_db()
    menu_items = clean_df(df)
    prompt = f"""
You are an expert lead scoring analyst. 
Evaluate how well these customer interests align with our food menu.

Food menu items (from database): {menu_items}

Customer interests: {interests}

Instructions:
- Check if each interest directly matches or closely relates to any menu item.
- Consider synonyms (e.g., "fries" vs "french fries").
- If an interest is not on the menu, mark it as a mismatch.
- Base your scoring only on the provided menu list.

Output format:
"Based on interest alignment, this lead has a [X]% likelihood of becoming a client.
Key factors:
- [bullet point 1]
- [bullet point 2]"
"""

    response = model.generate_content(prompt)
    response_data = {
        "query": query,
        "response": response.text
    }
    return response_data
