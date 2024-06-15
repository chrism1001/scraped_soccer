import requests
from bs4 import BeautifulSoup
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

data, count = supabase.table("Teams").delete().neq("id", 0).execute()

def insert_team_stats(data, conf):
    team_stats = data.find_all("tr")
    
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
            "conf": str(conf)
        }).execute()


with open("./Data/mls.txt", "r") as file:
    response = requests.get(file.read())
    soup = BeautifulSoup(response.text, "html.parser")
    
    eastern_data = soup.find(id="results2024221Eastern-Conference_overall")
    insert_team_stats(eastern_data, "Eastern")
        
    western_data = soup.find(id="results2024221Western-Conference_overall")
    insert_team_stats(western_data, "Western")