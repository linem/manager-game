import random
import time


def play_match(team1, team2):
    """Returns the score of the match based on the teams strength"""
    round = team1.matches_played + 1
    print(f"\nRound {round}: Home team {team1.name} against {team2.name}\n")

    home_court = random.choice(["team1", "team2"])
    home_court_advantage = 0.01
    team1_score_window = team1.strength * 0.4
    team2_score_window = 1 - (team2.strength * 0.4)
    close_penalty_size = 0.1

    if home_court == "team1":
        team1_score_window += home_court_advantage
    else:
        team2_score_window -= home_court_advantage

    team1_close_shot = [team1_score_window, team1_score_window + close_penalty_size]
    team2_close_shot = [team2_score_window, team2_score_window - close_penalty_size]
    team1_penalty = [team1_close_shot[1], team1_close_shot[1] + close_penalty_size]
    team2_penalty = [team2_close_shot[1], team2_close_shot[1] - close_penalty_size]

    match_score = [0, 0]
    for i in range(60):
        time.sleep(1)
        if i == 55:
            print("5 minutes left of the match!")
        shot = random.random()
        if shot < team1_score_window:
            match_score[0] += 1
            print_score(team1, match_score)
        elif shot > team2_score_window:
            match_score[1] += 1
            print_score(team2, match_score)
        elif team1_close_shot[0] < shot < team1_close_shot[1]:
            print_close_call(team1)
        elif team2_close_shot[0] < shot < team2_close_shot[1]:
            print_close_call(team2)
        elif team1_penalty[0] < shot < team1_penalty[1]:
            print_penalty(team1)
        elif team2_penalty[0] < shot < team2_penalty[1]:
            print_penalty(team2)

    announce_result(team1, team2, match_score)
    return [team1, team2, match_score]


def play_quiet_match(team1, team2):
    """Returns the score of the match based on the teams strength"""
    team1_score_window = team1.strength * 0.4
    team2_score_window = 1 - (team2.strength * 0.4)

    match_score = [0, 0]
    for i in range(80):
        shot = random.random()
        if shot < team1_score_window:
            match_score[0] += 1
        elif shot > team2_score_window:
            match_score[1] += 1
    return [team1, team2, match_score]


def print_score(team, match_score):
    padding = " " * (30 - len(team.name))
    print(f"{team.name} scores!{padding}({match_score[0]}:{match_score[1]})")


def print_close_call(team):
    print(f"{team.name} just missed the goal!")


def print_penalty(team):
    print(f"2 min penalty for {team.name}!")


def announce_result(team1, team2, match_score):
    score = f"({match_score[0]}:{match_score[1]})"
    if match_score[0] > match_score[1]:
        print(f"\n{team1.name} wins the match over {team2.name} {score}\n")
    elif match_score[0] < match_score[1]:
        score = f"({match_score[1]}:{match_score[0]})"
        print(f"\n{team2.name} wins the match over {team1.name} {score}\n")
    else:
        print(f"\n{team1.name} and {team2.name} played a draw {score}\n")
