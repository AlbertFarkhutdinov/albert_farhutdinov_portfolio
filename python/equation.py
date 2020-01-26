# the script works for equations with one root
import math


# Methods of solution
def half_division_method(function, minimum, maximum, accuracy):
    root = None
    step = 0
    while (maximum - minimum) >= accuracy:
        root = (minimum + maximum) / 2
        if function(minimum) * function(root) < 0:
            maximum = root
        else:
            minimum = root
        step += 1

    if function(root) < accuracy:
        return {'step': step, 'root': root}
    else:
        return None


def newton_method(function, minimum, maximum, accuracy, derivative):
    root = None
    step = 0
    segment = maximum - minimum
    while segment >= accuracy:
        if maximum != 0:
            root = maximum - (function(maximum) / derivative(maximum))
            segment = abs(root - maximum)
            maximum = root
            step += 1

    return {'step': step, 'root': root}


def iteration_method(function, minimum, maximum, accuracy, derivative_2):
    root = None
    segment = maximum - minimum
    value_1 = abs(derivative_2(minimum))
    value_2 = abs(derivative_2(maximum))
    if value_1 < 1 < value_2 or value_1 < value_2 < 1:
        step = 0
        while segment >= accuracy:
            root = minimum - function(minimum)
            segment = abs(root - minimum)
            minimum = root
            step += 1

        return {'step': step, 'root': root}
    elif value_2 < 1 < value_1 or value_2 < value_1 < 1:
        step = 0
        while segment >= accuracy:
            root = maximum - function(maximum)
            segment = abs(root - maximum)
            maximum = root
            step += 1

        return {'step': step, 'root': root}
    else:
        return None


# Current function and its first and second derivatives
def current_function(argument):
    return 3 * argument - 4 * math.log(argument) - 5


def current_derivative_1(argument):
    return 3 - 4 / argument


def current_derivative_2(argument):
    return - 2 + 4 / argument


if __name__ == '__main__':
    current_accuracy = 1e-6
    print('\nEquation:\n3 * x - 4 * ln(x) - 5 = 0\n')
    min_value = -1
    max_value = -2

    while min_value <= 0:
        min_value = float(input('Input x(min) > 0:\n'))

    while max_value <= min_value:
        max_value = float(input('Input x(max) > x(min):\n'))

    results = {
        'Half Division Method': half_division_method(current_function, min_value, max_value, current_accuracy),
        'Newton Method': newton_method(current_function, min_value, max_value, current_accuracy, current_derivative_1),
        'Iteration Method': iteration_method(current_function, min_value, max_value, current_accuracy,
                                             current_derivative_2),
    }

    print()
    for key, value in results.items():
        print(f'{key}:')
        if value:
            print(f'Step #{value["step"]}:\nx = {value["root"] : .5f}\n')
        else:
            print('This method is inefficient for given x(min) and x(max).\n')
