import os
import tkinter as tk
from winsound import *

from gui_functions import create_window, setup_ui, show_message, update_lives_display, disable_key
from game_logic import load_countries, choose_random_country, display_word, check_guess, check_win_condition, log_game_result, get_hint

import random

window = None
country = ''
guessed_letters = []
lives = 6
attempts = 0
ui = {}

def start_new_game():
    """Reset and start a new game"""
    global country, guessed_letters, lives, attempts, hint_given
        
    guessed_letters.clear()
    lives = 6
    attempts = 0

    countries = load_countries('data/countries.txt')
    country = choose_random_country(countries)   
    
    hint_given = False
    
    ui['word_label'].config(text = 
        f'{len(country)} letters \n{display_word(country, guessed_letters)} \nGuessed letters: {', '.join(guessed_letters)}', 
        font = ('Courier New Negrita', 20), fg = 'brown'
        )
    update_lives_display(ui['lives_label'], lives)

    for widget in ui['keyboard_frame'].winfo_children():
        widget.config(state='normal', bg='white')

def handle_guess(letter, button):
    """Handle when a player clicks a letter button"""
    global lives, attempts, hint_given

    is_correct = check_guess(letter, country)
    disable_key(button, correct = is_correct)
    
    guessed_letters.append(letter)
    attempts += 1

    if is_correct:
        ui['word_label'].config(text = 
        f'{len(country)} letters \n{display_word(country, guessed_letters)}\nGuessed letters: {', '.join(guessed_letters)}', 
        font = ('Courier New Negrita', 20), fg = 'brown'        
            )
        PlaySound('assets/right_letter.wav', SND_FILENAME)
        
    else:
        lives -= 1
        update_lives_display(ui['lives_label'], lives)
        ui['word_label'].config(text = 
        f'{len(country)} letters \n{display_word(country, guessed_letters)}\nGuessed letters: {', '.join(guessed_letters)}', 
        font = ('Courier New Negrita', 20), fg = 'brown'  
            )
        PlaySound('assets/wrong_letter.wav', SND_FILENAME)

    if check_win_condition(country, guessed_letters):
        PlaySound('assets/win_game.wav', SND_FILENAME)
        show_message('WIN', f'Congratulations, you win! The country was {country}.')
        log_game_result(country, 'WIN', attempts, guessed_letters)
        start_new_game()
        return
    
    if lives == 3 and not hint_given:
        show_message('Need a hint?', get_hint(country))
        hint_given = True
        
    if lives == 0:
        PlaySound('assets/fail_game.wav', SND_FILENAME)
        show_message('LOSE', f'No more lives! The country was {country}.')
        log_game_result(country, 'LOSE', attempts, guessed_letters)
        start_new_game()
        return

def main():
    global window, ui
    window, canvas, frame  = create_window()
    ui = setup_ui(window, canvas, frame, handle_guess, start_new_game)
    start_new_game()
    window.mainloop()

if __name__ == '__main__':
    main()