import random

# Core Game Functions
def load_countries(filename):
    """Load countries from file and return as a list"""
    with open(filename, 'r') as f:
        countries = [i for i in f.readlines()]
    return countries

def choose_random_country(countries_list):
    """Select and return a random country"""
    line = random.choice(countries_list)
    line = line.split(':')
    cregion, cname = line[0].strip(), line[-1].strip()
    return cname.upper()

def display_word(country, guessed_letters):
    """Display the current state of the word with revealed letters"""
    blank = []
    for letter in country:
        if letter.upper() in guessed_letters:
            blank.append(f'{letter} ')
        elif letter == ' ':
            blank.append('/ ')
        else:
            blank.append('_ ')
    return ''.join(blank)

def get_player_guess(guessed_letters):
    """Get and validate player's letter guess"""
    while True:
        guess = input('Enter a letter: ').upper()
        if len(guess) != 1 or not guess.isalpha():
            print('Not a letter. Try again: ')
        elif guess in guessed_letters:
            print('Letter already guessed.')
        else:
            return guess

def check_guess(letter, country):
    """Check if the guessed letter is in the country name"""
    return letter in country

def update_lives(lives, is_correct):
    """Update and return remaining lives"""
    if not is_correct:
        lives -= 1
    return lives

def check_win_condition(country, guessed_letters):
    """Check if player has won the game"""
    return all(letter in guessed_letters for letter in list(country) if letter != ' ') # checks if all is true

def check_lose_condition(lives):
    """Check if player has lost the game"""
    return lives == 0

# Logging Functions
def log_game_result(country, result, attempts, guessed_letters):
    """Save game result to log file"""
    with open('data/game_log.txt', 'a') as f:
        f.write(f'Country: {country} │ Result: {result} │ Attempts: {attempts}/6 │ Guessed Letters: {', '.join(guessed_letters)}\n')

# Extra Feature Functions
def get_hint(country):
    """Provide a hint about the country's region"""
    with open('data/countries.txt', 'r') as f:
        lines = f.readlines()
    for i in lines:
        i = i.split(':')
        cregion, cname = i[0].strip(), i[-1].strip()
        if cname.lower() == country.lower():
            region = cregion
            break
    return f'The country is located in {region}.'

# Main Game Loop
def play_game():
    """Main game loop that runs the entire game"""
    countries_list = load_countries("data/countries.txt")
    country = choose_random_country(countries_list)
    guessed_letters = []
    lives = 6
    attempts = 0

    print('Welcome to the Guess the Country!')
    
    while lives > 0:
        print(country)
        print(f'\nCountry has {len(country)} letters: ', display_word(country, guessed_letters))
        print(f'Guessed letters: {', '.join(guessed_letters)}')
        print(f'Lives left: {'❤️ '*lives}')
        
        if lives == 3:
            print(get_hint(country))
        
        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)
        is_correct = check_guess(guess, country)
        
        lives = update_lives(lives, is_correct)
        attempts += 1
        
        if check_win_condition(country, guessed_letters):
            print(f'Congratulations, you win! The country is {country}.')
            log_game_result(country, 'WIN', attempts, guessed_letters)
            break
        
        if check_lose_condition(lives):
            print(f'No more lives! The country was {country}.')
            log_game_result(country, 'LOSE', attempts, guessed_letters)
            break

def main():
    """Main function to start the game"""
    play_game()

if __name__ == "__main__":
    main()