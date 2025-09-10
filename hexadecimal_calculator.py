from collections import deque
symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def get_number(request):
    is_16 = False
    result = 0
    while not is_16:
        result = input(request)
        result = list(result.upper())
        if all((symbol in symbols) for symbol in result):
            is_16 = True
        else:
            print('Input error.')
    return result


def get_length(number_1, number_2):
    if len(number_1) < len(number_2):
        for _ in range(len(number_1), len(number_2)):
            number_1.appendleft('0')
    else:
        for _ in range(len(number_2), len(number_1)):
            number_2.appendleft('0')
    return len(number_1)


def get_symbol_index(symbol_index):
    if symbol_index > 15:
        spam = symbol_index // 16
        symbol_index = symbol_index % 16
    else:
        spam = 0
    return symbol_index, spam


def get_sum_of_numbers(number_1, number_2):
    length = get_length(number_1, number_2)
    number_1.reverse()
    number_2.reverse()
    result = deque()
    spam = 0
    for i in range(length):
        symbol_index = symbols.index(number_1[i]) + symbols.index(number_2[i]) + spam
        symbol_index, spam = get_symbol_index(symbol_index)
        result.appendleft(symbols[symbol_index])
    if spam:
        result.appendleft(symbols[spam])
    return result


def get_product_of_number_and_digit(number, digit):
    number.reverse()
    result = deque()
    spam = 0
    for i in range(len(number)):
        symbol_index = symbols.index(number[i]) * symbols.index(digit) + spam
        symbol_index, spam = get_symbol_index(symbol_index)
        result.appendleft(symbols[symbol_index])
    if spam:
        result.appendleft(symbols[spam])
    return result


def get_product_of_two_numbers(number_1, number_2):
    length = get_length(number_1, number_2)
    number_2.reverse()
    result = deque()
    for _ in range(length):
        result.append('0')

    for i in range(length):
        j = 0
        spam = get_product_of_number_and_digit(number_1.copy(), number_2[i])
        while j < i:
            spam.append('0')
            j += 1
        result = get_sum_of_numbers(result.copy(), spam)
    return result


if __name__ == '__main__':
    numbers = []
    for index in [0, 1]:
        input_string = f'Input {index + 1} hexadecimal number: '
        numbers.append(get_number(input_string))
        print(f'Number {index + 1}: {numbers[index]}')

    result_of_sum = get_sum_of_numbers(deque(numbers[0]), deque(numbers[1]))
    result_of_product = get_product_of_two_numbers(deque(numbers[0]), deque(numbers[1]))
    print(f'The sum of numbers: {"".join(result_of_sum)}')
    print(f'The product of numbers: {"".join(result_of_product)}')
