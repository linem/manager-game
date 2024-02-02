
import game
import game_schedule
import team


## Define teams
teams = []
with open("teams.csv") as file:
    for line in file:
        name, strength = line.strip().split(",")
        teams.append(team.Team(name, float(strength)))


## Scedule for each round of matches to be played
match_schedule = game_schedule.get_schedule(len(teams))


## Play match round
for match in match_schedule[1]:
    team1, team2 = match
    if team1 == 0:
        result = game.play_match(teams[team1], teams[team2])
    else:
        result = game.play_quiet_match(teams[team1], teams[team2])
    team.update_points(*result)
    team.update_score(*result)
    team.update_matches_played(*result[0:2])

print(vars(teams[0]))
print(vars(teams[1]))








