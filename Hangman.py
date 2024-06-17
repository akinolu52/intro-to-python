from random import randint


# a function to generate a random number based on the range entered


def generate_random_number(start_range, end_range):
    return randint(start_range, end_range)


# this function returns a single secret word from a list of secret_words
def get_secret_word():
    secret_words = ['python', 'java', 'perl', 'javascript', 'go']

    return secret_words[generate_random_number(0, len(secret_words) - 1)]


# **Display for Guesses:** Show underscores for un-guessed letters and reveal letters as they are guessed correctly.
def display_guesses(secret_word):
    return '_' * len(secret_word)


# **User Guesses:** Allow the player to input one letter at a time.
def get_user_guess():
    # a variable to bound the loop until the person guess a character
    is_right_input = False

    while not is_right_input:
        try:
            user_guess = input(
                '\nEnter a single character as your guess: ').lower()

            # check if it's a single character and if the character is an alphabet
            if len(user_guess) == 1 and user_guess.isalpha():
                # set is_right_input as true to exit the loop
                is_right_input = True

                # return the user_guess character
                return user_guess

            else:
                print("Please enter a single character ! \n")

        except ValueError:
            print("Please enter a single character ! \n")

        except Exception as exc:
            print(exc)


# a function to check if user_guess is equal to computer guess

# return index and display_guess if true and False if it's the wrong guess
def check_user_guess(user_guess, secret_word, display_guesses, previous_guessed_index):
    # get all the index at which this character exist
    indexes = [i for i, ltr in enumerate(secret_word) if ltr == user_guess]

    # if character is in the secret word
    if len(indexes) > 0:
        new_indexes = set()

        # check if all the indexes have been seen before
        if set(indexes) == previous_guessed_index:
            return False

        # if they have not all been seen before
        else:

            # check for new index not in previous guessed index
            for num in indexes:
                if num not in previous_guessed_index:
                    # add them to the result index
                    new_indexes.add(num)

        # if there are no new indexes
        if len(new_indexes) == 0:
            return False
        else:
            # for all new index
            for index in new_indexes:
                # a UI look for the guessed words
                display_guesses = display_guesses[:index] + \
                                  user_guess + display_guesses[index + 1:]

        # return new index and ui for guessed words
        return [new_indexes, display_guesses]

    # return value as it is not seen
    else:
        return False


# this return the hangman current state based on the index


def draw_hangman(index):
    full_hangman = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]

    # return the state of the hangman based on the index
    return full_hangman[index]


# a utility function to format how the current guess will look like
# it add space to the current_guess
def format_display(current_guess):
    return ' '.join(list(current_guess))


def hangman_game():
    # initialize variable for wrong guess
    wrong_guesses_count = 0
    # initialize variable for right guess
    correct_guesses_count = 0

    # initialize variable for the index of previously guessed character
    # using set since we don't want to repeat index
    previous_guessed_index = set()

    # generate a random computer guess
    secret_word = get_secret_word()

    print('Hello User! We will try and guess a word')

    # display the length with underscore
    secret_word_display = display_guesses(secret_word)

    print(format_display(secret_word_display))

    secret_word_count = len(secret_word)

    # loop until I've made the right guess or wrong guess count are 6
    while True:

        # display the current state of hangman
        print(draw_hangman(wrong_guesses_count))

        # check to see if I've made the right guess or wrong guess count are 6
        if wrong_guesses_count >= 6 or correct_guesses_count == secret_word_count:
            break

        # get the user guess input character
        user_guess = get_user_guess()

        # check the guessed word if it's wright or wrong
        result = check_user_guess(
            user_guess, secret_word, secret_word_display, previous_guessed_index)

        # for wrong guess
        if isinstance(result, bool):
            # print wrong guess
            print(user_guess, 'is a wrong value! ❌')

            # increment wrong guess count
            wrong_guesses_count += 1
            # print(wrong_guesses_count)

        # for right guess
        else:
            # get the index of the character and all the guessed word
            [index, secret_word_display] = result

            # add the index to the set of previously seen guesses
            previous_guessed_index.update(index)

            # print the words you've guessed properly
            print(format_display(secret_word_display))

            # increment the count of right guesses
            correct_guesses_count += len(index)

            # congratulation message if you guessed correctly
            if correct_guesses_count == len(secret_word):
                print('\nYou are correct 🥳🎉')

    # print the secret word
    print(f'secret word is "{secret_word}"')


hangman_game()
