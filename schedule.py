def plan_rules(x, n):
    if x == 1:
        x = n - 1
    elif 2 <= x < n:
        x -= 1
    return x


def get_schedule(n_teams):
    """Returns the team numbers in matches for each round"""
    if n_teams % 2 != 0:
        raise Exception("Number of teams must be even")
    first_col = list(range(0, int(n_teams / 2)))
    second_col = list(range(int(n_teams / 2), n_teams))[::-1]
    first_round = list(zip(first_col, second_col))

    schedule = {1: first_round}

    for i in range(1, n_teams - 1):
        round = i + 1
        next_round = []
        for match in schedule[i]:
            next_match = [plan_rules(team, n_teams) for team in match]
            next_round.append(next_match)
        schedule[round] = next_round
    return schedule

