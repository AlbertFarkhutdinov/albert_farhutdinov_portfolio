# Task:
# Build the dependence of mean value and dispersion of segment length beetween two point inside N-dimensional cube
# on number of dimensions. Edge length: 1 cm. The coordinates of a point: uniformly distributed random values.

from random import uniform
from math import sqrt
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def get_natural_number(question_string):
    number = 0
    is_int_positive = False
    while not is_int_positive:
        number = input(question_string)
        if number.isdigit():
            number = int(number)
            if number > 0:
                is_int_positive = True
        if not is_int_positive:
            print('Ошибка ввода.')
    return number


def get_mean_value(dimension, attempt_number):
    lengths = []
    lengths_2 = []
    dispersions = []
    dispersions_2 = []
    for attempt in range(attempt_number):
        difference_square = [(uniform(0, 1) - uniform(0, 1)) ** 2 for _ in range(dimension)]
        difference_square_sum = sum(difference_square)
        length = sqrt(difference_square_sum)
        lengths.append(length)
        lengths_2.append(difference_square_sum)
        dispersions.append(length / 6)
        dispersions_2.append(difference_square_sum / 36)
    mean_length = sum(lengths) / attempt_number
    mean_length_2 = sum(lengths_2) / attempt_number
    mean_dispersion = sum(dispersions) / attempt_number
    mean_dispersion_2 = sum(dispersions_2) / attempt_number
    coefficient = attempt_number / (attempt_number - 1)
    length_deviation = sqrt((mean_length_2 - mean_length ** 2) * coefficient)
    dispersion_deviation = sqrt((mean_dispersion_2 - mean_dispersion ** 2) * coefficient)
    return (mean_length, length_deviation), (mean_dispersion, dispersion_deviation)


def plot(title, y_label, x, values, filename):
    fig = plt.figure()
    plt.title(title)
    plt.xlabel('Number of dimensions')
    plt.ylabel(y_label)
    for value in values:
        plt.errorbar(x=x, y=value[0], yerr=value[1], fmt='.', color=value[2], label=value[3])
    plt.legend()
    fig.savefig(f'{filename}.svg')


def main(max_dimension, attempt_number):
    dimensions = [dimension for dimension in range(1, max_dimension + 1)]
    means = []
    mean_deviations = []
    dispersions = []
    dispersion_deviations = []
    for dimension in dimensions:
        mean, dispersion = get_mean_value(dimension, attempt_number)
        print(f'Done: {dimension}/{max_dimension}')
        means.append(mean[0])
        mean_deviations.append(mean[1])
        dispersions.append(dispersion[0])
        dispersion_deviations.append(dispersion[1])
    plot(title='Mean value and dispersion of segment length', y_label='Mean value [cm], dispersion [cm^2]',
         x=dimensions,
         values=[(means, mean_deviations, 'black', 'Mean value'),
                 (dispersions, dispersion_deviations, 'red', 'Dispersion')],
         filename='segment_length_and_dispersion')


if __name__ == '__main__':
    dimension_maximum = get_natural_number('Input maximum dimension number of the cube (natural number): ')
    print(f'Maximum dimension number of the cube: {dimension_maximum}\n')
    attempts = 1000
    print(f'Number of attempts at fixed value of dimension number: {attempts}\n')

    main(dimension_maximum, attempts)
