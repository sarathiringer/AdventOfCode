class Game:
    def __init__(self, first_player, outcome):
        self.first_player = first_player
        self.outcome = outcome
        self.second_player = None
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

        self.beats = {
            "paper": "rock",
            "rock": "scissors",
            "scissors": "paper"
        }

        self.beats_inv = {
            v: k for k, v in self.beats.items()
        }

    def get_start_points(self):
        self.points_second_player += self.start_points[self.second_player]
    
    def play(self):
        if self.first_player == self.second_player:
            self.points_second_player += 3
        else:
            winner = [
                v for k, v in self.rules.items() if sorted(k) == sorted((self.first_player, self.second_player))
            ][0]
            if self.second_player == winner:
                self.points_second_player += 6

    def decide_hand(self):
        if self.outcome == "lose":
            hand = self.beats[self.first_player]
            self.second_player = hand
        elif self.outcome == "draw":
            hand = self.first_player
            self.second_player = hand
        elif self.outcome == "win":
            hand = self.beats_inv[self.first_player]
            self.second_player = hand




mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

with open("2022/day-2/input.txt", "r") as f:
    lines = f.readlines()

points = 0

for line in lines:
    first_player, outcome = line.split()
    first_player = mapping[first_player]
    outcome = mapping[outcome]
    game = Game(first_player=first_player, outcome=outcome)
    game.decide_hand()
    game.get_start_points()
    game.play()
    points += game.points_second_player

print(points)
