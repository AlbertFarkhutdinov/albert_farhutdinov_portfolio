# the script works for systems with one solution
from fractions import Fraction


def check_size(minimum, maximum):
    size = ''
    condition = False
    while not condition:
        size = input(f'Input the size of matrix. A natural number from {minimum} to {maximum} is required.\n')
        if size.isdigit():
            size = int(size)
            condition = (minimum <= size <= maximum)

    return size


def get_fraction(number_string):
    if number_string.find('/') != -1:
        numerator = number_string.split('/')[0]
        denominator = number_string.split('/')[1]
    elif number_string.find('.') != -1:
        denominator = pow(10, len(number_string.split('.')[1]))
        numerator = float(number_string) * denominator
    else:
        numerator = number_string
        denominator = 1

    return Fraction(int(numerator), int(denominator))


def input_matrix(size):
    matrix = []
    for row in range(size):
        matrix.append([])
        for column in range(size):
            matrix[row].append(input(f'Input element [{row + 1}][{column + 1}]: '))
            matrix[row][column] = get_fraction(matrix[row][column])

        matrix[row].append(input(f'Input free member {row + 1}: '))
        matrix[row][size] = get_fraction(matrix[row][size])
        print()

    return matrix


def print_matrix(matrix):
    size = len(matrix)
    for row in range(size):
        for column in range(size):
            print(f'{matrix[row][column]}', end='\t')

        print(f'|\t{matrix[row][size]}\n')


if __name__ == '__main__':
    print('Solving a system of linear algebraic equations by the Gauss method\n')
    n = check_size(1, 15)
    print(f'\nThe size of matrix = {n} x {n + 1}')
    print('\nInput matrix of the system:\n')
    a = input_matrix(n)
    print('\nThe initial matrix: ')
    print_matrix(a)

    for j in range(n):
        column_array = []
        for i in range(n - j):
            column_array.append(abs(a[i + j][j]))

        for i in range(n - j):
            if a[i + j][j] == sorted(column_array)[-1]:
                a[j], a[i + j] = a[i + j], a[j]

        z = a[j][j]
        for k in range(n + 1):
            a[j][k] = a[j][k] / z

        for i in range(n - j - 1):
            z = a[i + j + 1][j]
            for k in range(n + 1):
                a[i + j + 1][k] = a[i + j + 1][k] - z * a[j][k]

    roots = []
    for j in range(n):
        root = a[n - 1 - j][n]
        roots.append(root)
        for i in range(n - 1 - j):
            a[n - 2 - j - i][n] = a[n - 2 - j - i][n] - root * a[n - 2 - j - i][n - 1 - j]
            a[n - 2 - j - i][n - 1 - j] = 0

    roots.append(a[0][n])

    print('The roots of the system: ')
    for i in range(n):
        print(f'x{i + 1} =', end=' ')
        print(roots[n - 1 - i], end=' ')
        print(f'or {roots[n - 1 - i] : .3f}')
