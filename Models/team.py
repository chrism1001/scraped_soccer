class Team:
    def __init__(self,
                 team_name,
                 record,
                 home_record,
                 away_record,
                 league_position,
                 goals,
                 goals_against,
                 diff,
                 next_match,
                 logo):
        self.team_name = team_name
        self.record = record
        self.home_record = home_record
        self.away_record = away_record
        self.league_position = league_position
        self.goals = goals
        self.goals_against = goals_against
        self.diff = diff
        self.next_match = next_match
        self.logo = logo
        