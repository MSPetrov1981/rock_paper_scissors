class ScoreBoard:
    def __init__(self, filename='scores.txt'):
        self.filename = filename
        self.user_wins = 0
        self.computer_wins = 0
        self.draw = 0
        self.load_scores()
    
    def update_score(self, winner):
        if winner == 'игрок':
            self.user_wins += 1
        elif winner == 'компьютер':
            self.computer_wins += 1
        else:
            self.draw +=1
        self.save_scores()
    
    def display_score(self):
        return f"Игрок: {self.user_wins} | Компьютер: {self.computer_wins} | Ничьи:{self.draw}"
    
    def save_scores(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(f"{self.user_wins},{self.computer_wins},{self.draw}")
    
    def load_scores(self):
        try:
            with open(self.filename, 'r') as f:
                scores = f.read().split(',')
                self.user_wins = int(scores[0])
                self.computer_wins = int(scores[1])
                self.draw = int (scores[2])
        except FileNotFoundError:
            self.user_wins = 0
            self.computer_wins = 0
            self.draw = 0
        except Exception as e:
            print(f"Ошибка загрузки результатов: {e}")