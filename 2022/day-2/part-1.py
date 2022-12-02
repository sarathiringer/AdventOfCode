class Game:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        self.hands = [first_player, second_player]
        self.points_second_player = 0

        self.start_points = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }

        self.rules = {
            ("paper", "rock"): "paper",
            ("rock", "scissors"): "rock",
            ("paper", "scissors"): "scissors",
        }

    def get_start_points(self):
        self.points_second_player += self.start_points[self.second_player]
    
    def play(self):
        if self.first_player == self.second_player:
            self.points_second_player += 3
        else:
            winner = [
                v for k, v in self.rules.items() if sorted(k) == sorted(self.hands)
            ][0]
            if self.second_player == winner:
                self.points_second_player += 6



mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

with open("2022/day-2/input.txt", "r") as f:
    lines = f.readlines()

points = 0

for line in lines:
    first_player, second_player = line.split()
    first_player = mapping[first_player]
    second_player = mapping[second_player]
    game = Game(first_player=first_player, second_player=second_player)
    game.get_start_points()
    game.play()
    points += game.points_second_player

print(points)
