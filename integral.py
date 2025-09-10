from math import log
from time import time
from input_functions import get_float_number, get_int_number


def function(arg):
    return arg * log(1 + pow(arg, 3))


def delta_function(arg1, arg2):
    if arg1 == arg2:
        return 1
    else:
        return 0


def integral_sum(left_border, right_border, interval_number, method):
    result = 0
    interval = (right_border - left_border) / interval_number

    for k in range(interval_number):
        x = left_border + interval * k
        result += function(x) * (delta_function(method, 0) + 0.5 * delta_function(method, 2))
        result += function(x + interval) * (delta_function(method, 1) + 0.5 * delta_function(method, 2))

    result = result * interval
    return result


def integral(left_border, right_border, interval_number, method):
    if method == 3:
        if interval_number % 2 != 0:
            interval_number += 1

        interval = (right_border - left_border) / interval_number
        result = function(left_border) - function(right_border)

        for k in range(int(interval_number / 2)):
            x = left_border + interval * 2 * k
            result += 4 * function(x + interval) + 2 * function(x + 2 * interval)

        result = result * interval / 3
    else:
        result = integral_sum(left_border, right_border, interval_number, method)

    return result


def improvement(left_border, right_border, interval_number, method, accuracy):
    time_of_start = time()
    current_value = integral(left_border, right_border, interval_number, method)
    previous_value = 0
    step = 1
    while abs(current_value - previous_value) >= accuracy:
        step += 1
        previous_value = current_value
        interval_number *= 2
        current_value = integral(left_border, right_border, interval_number, method)

    time_of_calculation = time() - time_of_start
    print(f'Integral = {current_value: .9f}.\nDone in {step} steps.\nTime of calculation: {time_of_calculation}.\n')


if __name__ == '__main__':
    print('\nIntegral #14\nf(x) = x * ln(1 + x^3)\n')
    current_accuracy = 1e-3
    min_value = get_float_number('Input x(min) > 0', minimum=current_accuracy)
    max_value = get_float_number('Input x(max) > x(min)', minimum=min_value + current_accuracy)
    number_of_intervals = get_int_number('Input number of intervals > 0', minimum=1)
    print()

    methods = [
        'Rectangle Method (Lower Sum)',
        'Rectangle Method (Upper Sum)',
        'Trapezium Method',
        "Simpson's Parabolic Method"
    ]

    for index, method_name in enumerate(methods):
        print(f'{index + 1}. {method_name}:')
        improvement(min_value, max_value, number_of_intervals, index, current_accuracy)
