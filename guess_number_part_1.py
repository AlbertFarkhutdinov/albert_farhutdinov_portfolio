from random import randint


def check_condition(request, condition):
    result = ''
    is_true = False
    while not is_true:
        result = input(f'{request}: ')
        is_true = condition(result)

    return result


if __name__ == '__main__':
    minimum = 1
    maximum = 100
    levels = {'1': 50, '2': 20, '3': 10, '4': 5, '5': 3}

    print(f'Game "Guess the number". Users guess the number from {minimum} to {maximum}, '
          f'that made up by the computer.\n')
    to_exit = ''
    while to_exit != '-1':
        number = randint(minimum, maximum)
        # print(number)

        level = check_condition('Select a level from 1 to 5', lambda x: x.isdigit() and 1 <= int(x) <= 5)
        max_count = levels[level]
        print(f'You selected the level {level}. You have {max_count} attempts.\n')

        user_count = int(check_condition('Input the number of players', lambda x: x.isdigit() and int(x) > 0))
        users = []
        print()
        for i in range(user_count):
            user_name = input(f'Input the name of player {i + 1}: ')
            users.append(user_name)

        print()
        attempt = 0
        user_number = 0
        is_winner = False
        winner_name = ''
        while not is_winner:
            attempt += 1
            if attempt > max_count:
                print('All players lost!')
                break
            for user in users:
                print(f'Player {user} moves.')
                user_number = int(check_condition(f'Input integer number from {minimum} to {maximum}',
                                                  lambda x: x.isdigit() and minimum <= int(x) <= maximum))
                if user_number == number:
                    is_winner = True
                    winner_name = user
                    break
                elif user_number < number:
                    print('The right number is more.\n')
                else:
                    print('The right number is less.\n')
        else:
            print(f'Player {winner_name} guessed the number with {attempt} attempts.')
        to_exit = check_condition('\nInput "-1" to quit or "1" to restart', lambda x: x in ['-1', '1'])
