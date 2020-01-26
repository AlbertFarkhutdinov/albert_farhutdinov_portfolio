from random import randint


def check_condition(request, condition):
    result = ''
    is_true = False
    while not is_true:
        result = input(f'{request}: ')
        is_true = condition(result)

    return result


if __name__ == '__main__':
    print('Game "Guess the number". Computer (C) guesses the number, that made up by the user (U).')
    to_exit = ''
    while to_exit != '-1':
        minimum = 1
        maximum = 100
        levels = {1: 15, 2: 10, 3: 5, 4: 3, 5: 1}

        dialogue = [
            '\nU: Hello, Computer!',
            f'I made up integer number from {minimum} to {maximum} for you.',
            'You have to guess it.',
            "C: Let's do it!",
            'U: Select a level from 1 to 5.'
        ]
        print('\n'.join(dialogue))
        level = randint(1, 5)
        max_count = levels[level]
        print(f'C: I selected level {level}.\nU: You have {max_count} attempts. Go!\n')
        attempt = 0
        number = 0
        computer_wins = False
        answer = None
        acceptable_answers = ['1', '2', '3', None]

        while not computer_wins:
            if answer in acceptable_answers:
                attempt += 1
                if answer == '1':
                    computer_wins = True
                    break
                elif answer == '2':
                    minimum = number + 1
                elif answer == '3':
                    maximum = number - 1
                if attempt > max_count and not computer_wins:
                    print('U: Computer, you lose!\nC: =(')
                    break
                if maximum - minimum < 0:
                    print('C: You are cheating!')
                    break
                number = randint(minimum, maximum)
                print(f'C: This is the number {number}.\n'
                      'Input 1, if I guessed it.\n'
                      'Input 2, if the right number is more.\n'
                      'Input 3, if the right number is less.')
                answer = input()
            else:
                print("C: I don't understand. Repeat.")
                answer = input()

        if computer_wins:
            print(f'U: You guessed the number with {attempt - 1} attempts!\nC: Hooray!')
        to_exit = check_condition('\nInput "-1" to quit or "1" to restart', lambda x: x in ['-1', '1'])
