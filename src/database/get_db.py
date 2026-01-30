import pandas as pd
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
DB_KEY = os.getenv("DB_KEY")


def get_db():
    supabase: Client = create_client(DB_URL, DB_KEY)
    response = supabase.table("burger_king_menu").select("*").execute()
    df = pd.DataFrame(response.data)
    print(df.info())
    return df


