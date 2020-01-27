def is_it_int_number(number):
    return number.isdigit() or (len(number) > 1 and number[0] == '-' and number[1:].isdigit())


def get_int_number(question, minimum=-float('inf'), maximum=float('inf')):
    int_number = 0
    is_number = False
    while not is_number:
        int_number = input(f'{question}:\n')
        if is_it_int_number(int_number):
            int_number = int(int_number)
            if minimum <= int_number <= maximum:
                is_number = True
            else:
                print(f'Input error. Your number is out of range [{minimum}; {maximum}].')
        else:
            print('Input error. Your number is not integer.')
    return int_number


def get_float_number(question, minimum=-float('inf'), maximum=float('inf')):
    float_number = 0
    is_float_number = False
    while not is_float_number:
        float_number = input(f'{question}:\n')
        if float_number.find('.') == float_number.rfind('.'):
            dot_position = float_number.find('.')
            condition_1 = (dot_position == -1 and is_it_int_number(float_number))
            condition_2 = (is_it_int_number(float_number[: dot_position]) and
                           is_it_int_number(float_number[dot_position + 1:]))
            if condition_1 or condition_2:
                float_number = float(float_number)
                if minimum <= float_number <= maximum:
                    is_float_number = True
                else:
                    print(f'Input error. Your number is out of range [{minimum}; {maximum}].')
        else:
            print('Input error. Your number is not float number.')
    return float_number


def bipolar_input(case_1, result_1, case_2, result_2):
    switch = ''
    while switch not in [case_1, case_2]:
        switch = input(f'Input {case_1} to {result_1} or {case_2} to {result_2}.\n')
    return switch


if __name__ == '__main__':
    choice = '1'
    while choice == '1':
        value_1 = get_int_number('Input integer number less than 100', maximum=99)
        value_2 = get_int_number('Input integer number more than 0', minimum=1)
        value_3 = get_int_number('Input integer number from 1 to 10', minimum=1, maximum=10)
        value_4 = get_int_number('Input integer number')
        value_5 = get_float_number('Input float number less than 100', maximum=99)
        value_6 = get_float_number('Input float number more than 0', minimum=1)
        value_7 = get_float_number('Input float number from 1 to 10', minimum=1, maximum=10)
        value_8 = get_float_number('Input float number')
        print(f'value_1 = {value_1}, value_2 = {value_2}, value_3 = {value_3}, value_4 = {value_4}')
        print(f'value_5 = {value_5}, value_6 = {value_6}, value_7 = {value_7}, value_8 = {value_8}')
        choice = bipolar_input('-1', 'quit', '1', 'restart')
