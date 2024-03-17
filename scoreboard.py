from tabulate import tabulate

def get_table_row(team):
    return [team.name, team.matches_played, team.points]

def print_scoreboard(teams):
    table_data = list(map(get_table_row, teams))
    table_data.sort(key=lambda table_data: table_data[2], reverse = True)

    print(tabulate(
        table_data,
        headers=["Team", "No games", "Points"],
        tablefmt='simple_grid')
    )





