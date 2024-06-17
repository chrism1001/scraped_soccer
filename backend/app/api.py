from fastapi import FastAPI
import os
from supabase import create_client
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


@app.get("/teams", tags=["teams"])
async def get_teams():
    try:
        data, count = supabase.from_("Teams")\
            .select("*")\
            .execute()
            
        return data
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error."}