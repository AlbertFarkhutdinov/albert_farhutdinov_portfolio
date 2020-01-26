# Task:
# A particle is born at point in time t0.
# 5 decays of this particle were recorded: 0.1, 0.15, 0.18, 0.3 and 0.33 seconds after birth.
# Determine the particle lifetime, using the maximum likelihood estimation (MLE).


from math import exp, log
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


# Probability distribution for decay of particle
def decay_probability_density(time, lifetime):
    return exp(-(time / lifetime)) / lifetime


# Natural logarithm of likelihood function
def log_likelihood_function(function, data, parameters):
    return sum([log(function(value, parameters)) for value in data])


# Dichotomy method for search of function's maximum on segment [min_value, max_value] accurate to value of accuracy
def dichotomy_method(function, data, min_value, max_value, accuracy):
    if (max_value - min_value) <= accuracy:
        return (min_value + max_value) / 2
    else:
        middle = (min_value + max_value) / 2
        dot_1 = middle - accuracy / 2
        dot_2 = middle + accuracy / 2
        value_1 = log_likelihood_function(function, data, dot_1)
        value_2 = log_likelihood_function(function, data, dot_2)
        if value_1 < value_2:
            return dichotomy_method(function, data, dot_1, max_value, accuracy)
        elif value_1 > value_2:
            return dichotomy_method(function, data, min_value, dot_2, accuracy)
        else:
            return (dot_1 + dot_2) / 2


def main():
    data = [0.1, 0.15, 0.18, 0.3, 0.33]
    min_time = min(data)
    max_time = max(data)
    accuracy = 2e-2
    result = dichotomy_method(decay_probability_density, data, min_time, max_time, accuracy)
    minimum = -log_likelihood_function(decay_probability_density, data, result)
    x_array = []
    y_array = []
    sigma_x = []
    sigma_y = []
    number_of_dots = 2001
    for i in range(number_of_dots):
        x = min_time + (2 * max_time - min_time) / (number_of_dots - 1) * i
        y = -log_likelihood_function(decay_probability_density, data, x)
        x_array.append(x)
        y_array.append(y)
        if abs(y - minimum - 0.5) <= 5 * 1e-3:
            sigma_x.append(x)
            sigma_y.append(y)

    left_sigma = result - sigma_x[0]
    right_sigma = sigma_x[-1] - result
    fig = plt.figure()
    plt.xlabel('Lifetime, sec')
    plt.ylabel('-ln(L)')
    plt.plot(x_array, y_array, color='black')
    x_result = [sigma_x[0], result, sigma_x[-1]]
    y_result = [sigma_y[0], minimum, sigma_y[-1]]
    plt.scatter(x_result, y_result, color='red')
    plt.title(f'Lifetime: t = ({result: .2f} + {right_sigma: .2f} - {left_sigma: .2f}) sec.')
    fig.savefig('minus_log_of_likelihood_function.svg')


if __name__ == '__main__':
    main()
