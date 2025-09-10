from random import randint
import time


def generate_number(length):
    digits = []
    min_value = 1
    max_value = 9
    digits.append(randint(min_value, max_value))
    for position in range(length - 1):
        new_digit = digits[0]
        while new_digit in digits:
            new_digit = randint(min_value, max_value)

        digits.append(new_digit)
    return digits


def check_input(all_digits):
    number = ''
    condition = False
    while not condition:
        number = input('Input number (-1 to finish game).\n')
        condition = (len(str(number)) == all_digits and (number.isdigit() or number == '-1'))

    return int(number)


def check_number(question, answer):
    result = {'win': False, 'bulls': 0, 'cows': 0}
    string_of_digits = str(answer)
    for i in range(len(string_of_digits)):
        if int(string_of_digits[i]) == question[i]:
            result['bulls'] += 1
        elif int(string_of_digits[i]) in question:
            result['cows'] += 1
    if result['bulls'] == number_of_digits:
        result['win'] = True
     
    return result


def guess_number(attempts):
    game_is_running = True
    while game_is_running:
        my_number = check_input(number_of_digits)
        attempts += 1
        if my_number == -1:
            game_is_running = False
        else:
            result = check_number(random_number, my_number)
            if result['win']:
                print(f"Congratulations! You guessed the number. Attempts: {attempts}")
                game_is_running = False
                time.sleep(5)
            else:
                print(f"Bulls: {result['bulls']}. Cows: {result['cows']}.")


if __name__ == '__main__':
    number_of_digits = 4
    number_of_attempts = 0
    rules = ['The game "Bulls and Cows".\n',
             f'The computer makes up a {number_of_digits}-digit number. You have to guess this number.\n',
             'The computer gives a clue in the form of bulls and cows after each attempt.\n',
             'This is a bull, if you guessed both a digit and its position in the number.\n',
             'This is a cow, if you guessed a digit of the number, but not its position.\n',
             f'Thus, the goal of the game is to get the number of bulls equal to {number_of_digits}.\n\n'
             ]
    print(''.join(rules))
    random_number = generate_number(number_of_digits)
    # print(random_number)
    guess_number(number_of_attempts)
