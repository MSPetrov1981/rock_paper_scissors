import random

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'ничья'
    winning_combinations = {
        'камень': 'ножницы',
        'ножницы': 'бумага',
        'бумага': 'камень'
    }
    if winning_combinations[user_choice] == computer_choice:
        return 'игрок'
    return 'компьютер'