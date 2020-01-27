from input_functions import get_float_number, get_int_number


def function(arg, param):
    return param*pow(arg, 2)


if __name__ == '__main__':
    print('Function tabulation\nf(x) = A * x^2.\n')
    parameter = get_float_number('Input the value of parameter A')
    first_value = get_float_number('Input first value of x')
    last_value = get_float_number('Input last value of x')
    number_of_dots = get_int_number('Input number of dots more than 1', minimum=2)
    for i in range(number_of_dots):
        x = first_value + i * (last_value - first_value)/(number_of_dots-1)
        print(f'x = {x : .6f}, f(x) = {function(x, parameter) : .6f};')

    print('Done!')
