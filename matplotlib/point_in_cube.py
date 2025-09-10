# There is cube. Edge length: 1. 10 points are randomly located inside the cube.
# The coordinates of a point: uniformly distributed random values.
# Find the point such that the sum of the exponents of the distances from this point to other ones is minimal.


from random import uniform
from math import sqrt, exp
from iminuit import Minuit


def print_point(point):
    result = '('
    for x in point:
        result += f'{x: .3f}, '.lstrip(' ')
    result = result.rstrip(', ') + ')'
    print(result)


def distance_between_points(point_1, point_2, number_of_dimensions):
    return sqrt(sum([(point_1[index] - point_2[index]) ** 2 for index in range(number_of_dimensions)]))


def get_random_point(number_of_dimensions):
    return [uniform(0, 1) for _ in range(number_of_dimensions)]


def minimized_function(required_point, points, number_of_dimensions):
    result_array = [exp(distance_between_points(required_point, point, number_of_dimensions)) for point in points]
    return sum(result_array)


def minimization(number_of_dimensions, number_of_points):
    points = [get_random_point(number_of_dimensions) for _ in range(number_of_points)]
    print('Initial points')
    for point in points:
        print_point(point)

    start_point = get_random_point(number_of_dimensions)

    def new_minimized_function(required):
        return minimized_function(required, points, number_of_dimensions)

    minuit = Minuit.from_array_func(fcn=new_minimized_function, start=start_point, error=1, errordef=0.5)
    minuit.migrad()
    print('\nRequired point:')
    print_point([minuit.values[i] for i in range(len(minuit.values))])


if __name__ == '__main__':
    minimization(number_of_dimensions=3, number_of_points=10)
