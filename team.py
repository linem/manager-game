class Team:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.points = 0
        self.score = 0
        self.matches_played = 0


def update_points(team1, team2, match_score):
    """Updates the teams points after a match"""
    points_for_win = 3
    points_for_draw = 1

    if match_score[0] > match_score[1]:
        team1.points += points_for_win
    elif match_score[0] < match_score[1]:
        team2.points += points_for_win
    else:
        team1.points += points_for_draw
        team2.points += points_for_draw


def update_score(team1, team2, match_score):
    """Updates the team score after a match"""
    team1.score += match_score[0] - match_score[1]
    team2.score += match_score[1] - match_score[0]


def update_matches_played(team1, team2):
    """Updates the number of matches played"""
    team1.matches_played += 1
    team2.matches_played += 1
