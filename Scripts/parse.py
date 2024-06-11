import requests
from bs4 import BeautifulSoup
import os

def insert_team_stats(conf):
    team_stats = conf.find_all("tr")
    
    for team_stat in team_stats:
        team_name = team_stat.find("a", href=True)
        if not team_name:
            continue
        
        team_rank = team_stat.find("th", attrs={"data-stat": "rank"})
        
        team_games = team_stat.find("td", attrs={"data-stat": "games"})
        
        team_wins = team_stat.find("td", attrs={"data-stat": "wins"})
        
        team_ties = team_stat.find("td", attrs={"data-stat": "ties"})
        
        team_losses = team_stat.find("td", attrs={"data-stat": "losses"})
        
        team_goals_for = team_stat.find("td", attrs={"data-stat": "goals_for"})
        
        team_goals_against = team_stat.find("td", attrs={"data-stat": "goals_against"})
        
        team_goal_diff = team_stat.find("td", attrs={"data-stat": "goal_diff"}) 
        
        team_attendance_per_game = team_stat.find("td", attrs={"data-stat": "attendance_per_g"})
    

with open("./Data/mls.txt", "r") as url:
    response = requests.get(url.read())
    soup = BeautifulSoup(response.text, "html.parser")
    
    eastern_conf = soup.find(id="results2024221Eastern-Conference_overall")
    insert_team_stats(eastern_conf)
        
    western_conf = soup.find(id="results2024221Western-Conference_overall")
    insert_team_stats(western_conf)