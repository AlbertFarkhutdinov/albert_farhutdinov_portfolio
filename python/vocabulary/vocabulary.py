from random import randint as rand


def dictionary():
    with open('vocabulary.txt', 'r') as file:
        data = file.readlines()
        score = 0
        total = 0
        repeat = []
        is_continue = True
        while is_continue:
            i = rand(0, len(data) - 1)
            pair = data[i].rstrip('\n')
            pair = pair.split(' - ')
            question = pair[0]
            right = pair[1]
            print(question, end=' - ')
            answer = input()

            if answer == right:
                print('Right!')
                score += 1
            else:
                print('Wrong!')
                print(right)
                repeat.append(question)

            total += 1
            agree = ''
            while agree not in ['0', '1']:
                agree = input('1 to continue. 0 to finish: ')
            if agree == '0':
                is_continue = False

        print('Done! Right answers: %d/%d' % (score, total))
        if score != total:
            repeat = set(repeat)
            print(f'Repeat these words:\n{repeat}')


if __name__ == '__main__':
    dictionary()
