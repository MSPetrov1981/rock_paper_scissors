import tkinter as tk
from tkinter import messagebox
from game import get_computer_choice, determine_winner
from scoreboard import ScoreBoard

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.scoreboard = ScoreBoard()
        
        # Создание элементов интерфейса
        self.label = tk.Label(root, text="Choose your weapon!", font=('Arial', 14))
        self.label.pack(pady=20)
        
        self.score_label = tk.Label(root, text=self.scoreboard.display_score(), font=('Arial', 12))
        self.score_label.pack()
        
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=20)
        
        self.rock_btn = tk.Button(buttons_frame, text="Rock", command=lambda: self.play('rock'))
        self.rock_btn.grid(row=0, column=0, padx=10)
        
        self.paper_btn = tk.Button(buttons_frame, text="Paper", command=lambda: self.play('paper'))
        self.paper_btn.grid(row=0, column=1, padx=10)
        
        self.scissors_btn = tk.Button(buttons_frame, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_btn.grid(row=0, column=2, padx=10)
        
        self.quit_btn = tk.Button(root, text="Quit", command=root.quit)
        self.quit_btn.pack(pady=20)
    
    def play(self, user_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            result_text = f"You win! Computer chose {computer_choice}"
            self.scoreboard.update_score('user')
        elif winner == 'computer':
            result_text = f"You lose! Computer chose {computer_choice}"
            self.scoreboard.update_score('computer')
        else:
            result_text = f"Draw! Computer also chose {computer_choice}"
        
        self.score_label.config(text=self.scoreboard.display_score())
        messagebox.showinfo("Result", result_text)