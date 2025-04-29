class BasketBall:
    def __init__(self):
        self.team1_score = 0
        self.team2_score = 0

    def update_team1_score(self, points):
        self.team1_score += points

    def update_team2_score(self, points):
        self.team2_score += points

    def print_score(self):
        print(f"Team 1: {self.team1_score} | Team 2: {self.team2_score}")



# Create an object of the class.
game = BasketBall()

# Update scores using your methods.
game.update_team1_score(3)
game.update_team2_score(2)

# Print the score.
game.print_score()
