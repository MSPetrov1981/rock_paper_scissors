class ScoreBoard:
    def __init__(self, filename='scores.txt'):
        self.filename = filename
        self.user_wins = 0
        self.computer_wins = 0
        self.load_scores()
    
    def update_score(self, winner):
        if winner == 'user':
            self.user_wins += 1
        elif winner == 'computer':
            self.computer_wins += 1
        self.save_scores()
    
    def display_score(self):
        return f"Player: {self.user_wins} | Computer: {self.computer_wins}"
    
    def save_scores(self):
        with open(self.filename, 'w') as f:
            f.write(f"{self.user_wins},{self.computer_wins}")
    
    def load_scores(self):
        try:
            with open(self.filename, 'r') as f:
                scores = f.read().split(',')
                self.user_wins = int(scores[0])
                self.computer_wins = int(scores[1])
        except FileNotFoundError:
            self.user_wins = 0
            self.computer_wins = 0
        except Exception as e:
            print(f"Error loading scores: {e}")