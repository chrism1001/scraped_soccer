from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os
from supabase import create_client
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

BASE_DIR = Path(__file__).resolve().parent
app.mount("/assets", StaticFiles(directory=str(Path(BASE_DIR, "templates/assets"))), name="assets")
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_teams")
async def get_teams():
    try:
        data, count = supabase.from_("Teams")\
            .select("*")\
            .execute()
            
        return { "data": data[1] }
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error."}
    
@app.get("/get_teams_eastern")
async def get_teams():
    try:
        data, count = supabase.from_("Teams")\
            .select("*")\
            .eq("conf", "Eastern Conference")\
            .order("rank", desc=False)\
            .execute()
            
        return { "data": data[1] }
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error."}
    
@app.get("/get_teams_western")
async def get_teams():
    try:
        data, count = supabase.from_("Teams")\
            .select("*")\
            .eq("conf", "Western Conference")\
            .order("rank", desc=False)\
            .execute()
            
        return { "data": data[1] }
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error."}
