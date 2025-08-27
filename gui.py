import tkinter as tk
from tkinter import messagebox
from game import get_computer_choice, determine_winner
from scoreboard import ScoreBoard

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Камень-ножницы-бумага")
        self.scoreboard = ScoreBoard()
        
        # Создание элементов интерфейса
        self.label = tk.Label(root, text="выберите ваш ход", font=('Arial', 14))
        self.label.pack(pady=20)
        
        self.score_label = tk.Label(root, text=self.scoreboard.display_score(), font=('Arial', 12))
        self.score_label.pack()
        
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=20)
        
        self.rock_btn = tk.Button(buttons_frame, text="камень", command=lambda: self.play('камень'))
        self.rock_btn.grid(row=0, column=0, padx=10)
        
        self.paper_btn = tk.Button(buttons_frame, text="бумага", command=lambda: self.play('бумага'))
        self.paper_btn.grid(row=0, column=1, padx=10)
        
        self.scissors_btn = tk.Button(buttons_frame, text="ножницы", command=lambda: self.play('ножницы'))
        self.scissors_btn.grid(row=0, column=2, padx=10)
        
        self.quit_btn = tk.Button(root, text="Выход", command=root.quit)
        self.quit_btn.pack(pady=20)
    
    def play(self, user_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'игрок':
            result_text = f"Вы победили! Компьютер выбрал {computer_choice}"
            self.scoreboard.update_score('игрок')
        elif winner == 'компьютер':
            result_text = f"Вы проиграли! Компьютер выбрал {computer_choice}"
            self.scoreboard.update_score('компьютер')
        else:
            result_text = f"Ничья! компьютер выбрал {computer_choice}"
            self.scoreboard.update_score ('ничья')
        
        self.score_label.config(text=self.scoreboard.display_score())
        messagebox.showinfo("Результат", result_text)