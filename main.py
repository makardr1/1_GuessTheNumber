# Guess the number
# Description: the computer will choose a random number, and the players will have to take turns guessing the number
from random import randint


def number_of_players(launch: str) -> int:
    print(launch)
    try:
        number = int(input())
        return number
    except ValueError:
        return number_of_players("Please enter a natural number")


start = number_of_players("Enter the number of players")


def player_names(number: int) -> dict:
    print("Enter player names")
    list_of_players = {i: input() for i in range(1, number + 1)}
    print("List of players:")

    for key, value in list_of_players.items():
        if key == len(list_of_players):
            print(f"{key}. {value}.")
        else:
            print(f"{key}. {value};")
    return list_of_players


players = player_names(start)


def game(correction: str, game_players: dict, key=1) -> str:
    print(correction)
    try:
        n_1, n_2 = int(input()), int(input())
        random_number = randint(n_1, n_2)
    except ValueError:
        return game("The first number must be less than the second or the input data must be natural numbers",
                    game_players)
    print(f"Your range is from {n_1} to {n_2}")
    print("The game has begun!")

    while True:
        try:
            if key > len(game_players):
                key = 1
            print(f"{game_players[key]}, enter a natural number")
            new_number = int(input())
            if new_number == random_number:
                return f"{game_players[key]} won, congratulations!"
        except ValueError:
            print("You're missing a move because the number is entered incorrectly")
        key += 1


print(game("Enter 2 numbers to indicate the range", players))
