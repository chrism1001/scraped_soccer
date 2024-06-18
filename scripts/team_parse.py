import requests
from bs4 import BeautifulSoup
import os
from supabase import create_client
from dotenv import load_dotenv
import re
import time

load_dotenv()
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

data, count = supabase.table("Teams").delete().neq("id", 0).execute()

def insert_team_data(soup, team_id):
    team_logo = soup.find("img", class_="teamlogo")["src"]
    team_conf = soup.find("span", id=re.compile("ern-Conference_overall"))["data-label"].split(",")[0]
    
    team_overall_stats = soup.find("table", id=re.compile("ern-Conference_overall"))
    
    team_stats = team_overall_stats.find_all("tr", class_="hilite bold")
    
    for team_stat in team_stats:
        team_name = team_stat.find("a", href=True)
        if not team_name:
            continue
        team_name = team_name.text.strip()
        team_rank = team_stat.find("th", attrs={"data-stat": "rank"}).text.strip()
        team_games = team_stat.find("td", attrs={"data-stat": "games"}).text.strip()
        team_wins = team_stat.find("td", attrs={"data-stat": "wins"}).text.strip()
        team_ties = team_stat.find("td", attrs={"data-stat": "ties"}).text.strip()
        team_losses = team_stat.find("td", attrs={"data-stat": "losses"}).text.strip()
        team_goals_for = team_stat.find("td", attrs={"data-stat": "goals_for"}).text.strip()
        team_goals_against = team_stat.find("td", attrs={"data-stat": "goals_against"}).text.strip()
        team_goal_diff = team_stat.find("td", attrs={"data-stat": "goal_diff"}) .text.strip()
        team_attendance_per_game = team_stat.find("td", attrs={"data-stat": "attendance_per_g"}).text.strip()
        team_attendance_per_game = team_attendance_per_game.replace(",", "")
        
        data, count = supabase.table("Teams").insert({
            "id": str(team_id),
            "team_name": str(team_name),
            "games": int(team_games),
            "wins": int(team_wins),
            "ties": int(team_ties),
            "losses": int(team_losses),
            "goals_for": int(team_goals_for),
            "goals_against": int(team_goals_against),
            "goals_diff": int(team_goal_diff),
            "attendance_per_game": int(team_attendance_per_game),
            "rank": int(team_rank),
            "conf": str(team_conf),
            "team_logo": str(team_logo)
        }).execute()
        
        break

pages = 0
with open("./data/teams.txt", "r") as file:
    for url in file:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        team_id = url.split("/")[5]
        
        insert_team_data(soup, team_id)
        
        pages += 1
        if pages == 10:
            time.sleep(60)
            pages = 0
        
        