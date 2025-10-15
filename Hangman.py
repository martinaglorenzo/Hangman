import random                              # for choosing a random country

def load_countries():
    countries = []
    with open("countries.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                countries.append(line)
    return countries


def choose_random_country(countries):     
    country = random.choice(countries)      # Pick one random country and return it in uppercase
    return country.upper()


def make_display(country, guessed_letters): # for creating word display
    display = ""
    for letter in country:
        if letter == " ":
            display += "/"              # replacing spaces with slashes
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"              # replacing letters with an underscore
    return display


def is_valid_guess(guess, guessed_letters):   # checks if guess is valid
    if len(guess) != 1:
        print("Please enter only one letter.")
        return False
    if not guess.isalpha():
        print("Please enter a letter (A–Z).")
        return False
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return False
    return True


def check_win(country, guessed_letters):
    # Return True if all letters have been guessed
    for letter in country:
        if letter.isalpha() and letter not in guessed_letters:
            return False
    return True


def play_game():                          # MAIN GAME LOOP
    countries = load_countries()
    country = choose_random_country(countries)
    guessed_letters = []
    tries_left = 5

    print("Hello! Guess my country!")

    while True:
        display = make_display(country, guessed_letters)
        print("\nCountry:", display)
        print("Tries left:", tries_left)

        if check_win(country, guessed_letters):
            print("🎉 You guessed it! The country was:", country.title())
            break

        guess = input("Guess a letter: ").upper()

        if not is_valid_guess(guess, guessed_letters):
            continue

        guessed_letters.append(guess)

        if guess in country:
            print("Good guess!")
        else:
            print("Wrong guess.")
            tries_left -= 1

        if tries_left == 0:
            print("\n❌ No more tries left. The country was:", country.title())
            break


play_game()                                 # RUN GAME