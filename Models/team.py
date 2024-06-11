class Team:
    def __init__(self,
                 team_name,
                 rank,
                 games,
                 wins,
                 ties,
                 losses,
                 goals_for,
                 goals_against,
                 goals_diff,
                 attendance_per_game):
        self.team_name = team_name
        self.rank = rank,
        self.games = games
        self.wins = wins
        self.ties = ties
        self.losses = losses
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.goals_diff = goals_diff
        self.attendance_per_game = attendance_per_game
        