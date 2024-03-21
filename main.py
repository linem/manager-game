import game
import schedule
import team
import scoreboard

N_TEAMS = 18


def main():
    my_team = prepare_my_team()
    teams = get_list_of_all_teams(my_team, "teams.csv")
    match_schedule = schedule.get_schedule(len(teams))

    while True:
        next_step = input("Choose [PLAY], [SCORE]: ").lower()

        if next_step in ["score", "s"]:
            scoreboard.print_scoreboard(teams)

        elif next_step in ["play", "p"]:
            play_next_round(teams, match_schedule)

        elif next_step == "end":
            exit()

        else:
            print_help_message()


def prepare_my_team():
    my_team_city = input("Choose a team city: ").title().replace(" ", "")
    my_team_name = input("Choose a team name: ").upper().replace(" ", "")
    if len(my_team_city) == 0:
        my_team = team.Team("Manchester ROCKS", 0.66)
    else:
        my_team = team.Team(f"{my_team_city} {my_team_name}", 0.66)
    return my_team


def get_list_of_all_teams(my_team, teams_file):
    teams = [my_team]
    with open(teams_file) as file:
        for line in file:
            name, strength = line.strip().split(",")
            if name.split(" ")[0] != my_team.name.split(" ")[0]:
                teams.append(team.Team(name, float(strength)))
            if len(teams) == N_TEAMS:
                break
    return teams


def play_next_round(teams, match_schedule):
    this_round_number = teams[0].matches_played + 1
    for match in match_schedule[this_round_number]:
        team1, team2 = match
        if team1 == 0:
            result = game.play_match(teams[team1], teams[team2])
        else:
            result = game.play_quiet_match(teams[team1], teams[team2])
        team.update_points(*result)
        team.update_score(*result)
        team.update_matches_played(*result[0:2])


def print_help_message():
    print(
        (
            "\n"
            "--- HELP ---\n"
            "Type PLAY and press enter to play the next match round \n"
            "Type SCORE and press enter to see the scoreboard \n"
            "Type END and press enter to end game \n"
        )
    )


if __name__ == "__main__":
    main()
