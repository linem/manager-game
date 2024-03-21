def plan_rules(x):
    """Logic for next round in match planning for 18 teams"""
    if x in range(1, 8):
        x += 1
    elif x == 8:
        x += 9
    elif x == 9:
        x -= 8
    elif x in range(10, 18):
        x -= 1
    return x


def get_schedule(number_of_teams):
    """Returns the team numbers in matches for each round"""
    if number_of_teams != 18:
        raise Exception("Not implemented for teams != 18")
    match_plan = {
        1: [
            [0, 9],
            [1, 10],
            [2, 11],
            [3, 12],
            [4, 13],
            [5, 14],
            [6, 15],
            [7, 16],
            [8, 17],
        ]
    }
    for i in range(1, 17):
        round = i + 1
        next_round_plan = []
        for match in match_plan[i]:
            new_match = [plan_rules(team_num) for team_num in match]
            next_round_plan.append(new_match)
        match_plan[round] = next_round_plan
    return match_plan
