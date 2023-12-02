import numpy as np

base_path = "/Users/sarathiringer/DEV/projects/AdventOfCode/2023/day-2/"

with open(base_path + "input.txt", "r") as f:
    lines = f.readlines()

game_power = 0

for line in lines:
    line = line.strip()
    # Get text up until first colon, then pick the digit from that
    game, revealed_sets = line.split(":")
    minimal_game = {"green": 0, "red": 0, "blue": 0}
    for revealed_set in revealed_sets.split(";"):
        revealed_set = revealed_set[1:]
        # Get the color and the number of cubes
        for num_and_color in revealed_set.split(", "):
            number, color = num_and_color.split(" ")
            number = int(number)
            if number > minimal_game[color]:
                minimal_game[color] = number
    game_power += np.product(list(minimal_game.values()))

print(f"Total game power: {game_power}")
