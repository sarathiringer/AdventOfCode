base_path = "/Users/sarathiringer/DEV/projects/AdventOfCode/2023/day-2/"

with open(base_path + "input.txt", "r") as f:
    lines = f.readlines()

# Config: 12 red cubes, 13 green cubes, and 14 blue cubes
conf = {"green": 13, "red": 12, "blue": 14}

possible_game_sum = 0

for line in lines:
    line = line.strip()
    # Get text up until first colon, then pick the digit from that
    game, revealed_sets = line.split(":")
    game_nr = int(game.split(" ")[-1])
    game_possible = []
    for revealed_set in revealed_sets.split(";"):
        revealed_set = revealed_set[1:]
        # Get the color and the number of cubes
        for num_and_color in revealed_set.split(", "):
            number, color = num_and_color.split(" ")
            if int(number) <= conf[color]:
                game_possible.append(True)
            else:
                game_possible.append(False)
    if all(game_possible):
        possible_game_sum += game_nr

print(f"Sum of possible games: {possible_game_sum}")
