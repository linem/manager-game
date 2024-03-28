import time
import random
import string


def train_team():
    
    print_train_intro()
    input("Are you ready to start? ")

    rounds = 10
    total_elapsed_time = 0
    correct_responses = 0

    for i in range(1, rounds + 1):
        goal = random.choice(string.ascii_letters)
        start_time = time.time()
        response = input(f"Type {goal}, then enter: ")
        if response == goal:
            end_time = time.time()
            elapsed_time = end_time - start_time
            correct_responses += 1
        else:
            elapsed_time = 5
        total_elapsed_time += elapsed_time

    average_time = round(total_elapsed_time / rounds, 2)

    print(f"\nYou had {correct_responses} out of {rounds} correct")
    if correct_responses != rounds:
        print("For each wrong character you get a penalty of 5 seconds")
    print(f"Your average response time was\n{average_time} seconds")

    bonus_strength = get_bonus_strength(average_time)

    return bonus_strength


def print_train_intro():
    print(
        "",
        "TRAINING MODE",
        "Type the characters as fast as you can.",
        "The faster you type the correct character",
        "and hit Enter, the better your training will",
        "be and your team will increase their performance.",
        "",
        sep="\n",
    )


def get_bonus_strength(average_time):
    if average_time < 1:
        print("Excellent! You have increased your team's performance by 2%\n")
        bonus_strength = 0.02
    elif average_time < 1.5:
        print("Good job! You have increased your team's performance by 1%\n")
        bonus_strength = 0.01
    else:
        print(
            "Your reaction time was too slow to boost your team's performance. "
            "You can try again after the next match.\n"
        )
        bonus_strength = 0

    return bonus_strength
