# Task:
# There are N = 1000 hamsters.
# Mean value of dead hamsters per time unit: N * death_percent, where death_percent = death_coefficient
# Mean value of born hamsters per time unit: N * birth_percent, where birth_percent = birth_coefficient / N^2,
# death_coefficient = 0.01,
# birth_coefficient = 10000
# Build dependence of hamsters mean value on time.

from random import uniform
import math
import matplotlib.pyplot as plot
plot.style.use('seaborn-whitegrid')


# Function, which returns array of ln(x!) for x in range(total).
# It is used below for optimization of poisson function.
def get_log_factorial(total):
    logs = [math.log(x) if x != 0 else 0 for x in range(total)]
    log_factorial = [0] * total
    for x in range(2, total):
        log_factorial[x] += (log_factorial[x - 1] + logs[x])
    return log_factorial


# Random number generator for numbers, that obey Poisson's distribution
# mean_value - required expected value, total - maximum allowable value
def poisson(mean_value, total, log_factorial):
    log_mean = 0 if mean_value == 0 else math.log(mean_value)
    y_array = [math.exp(x * log_mean - mean_value - log_factorial[x]) for x in range(total)]
    sum_of_values = sum(y_array)
    if sum_of_values == 0:
        return total
    normalized_values = [value / sum_of_values for value in y_array]
    random_value = uniform(0, 1)
    for x, value in enumerate(normalized_values):
        if random_value > value:
            random_value -= value
        else:
            return x + 1


def get_mean_dependence(death_coefficient, birth_coefficient, realizations_number, total_time, start_number):
    log_factorial = get_log_factorial(start_number)
    death_percent = death_coefficient
    mean_dependence = [0] * (total_time + 1)
    dispersion_dependence = [0] * (total_time + 1)
    deviation_dependence = [0] * (total_time + 1)
    for realization in range(realizations_number):
        total_number = start_number
        mean_dependence[0] += total_number / realizations_number
        dispersion_dependence[0] += total_number ** 2 / realizations_number
        for time_unit in range(1, total_time + 1):
            deaths_number = poisson(death_percent * total_number, total_number, log_factorial)
            birth_percent = birth_coefficient / (total_number ** 2)
            mean_birth_number = int(birth_percent * total_number)
            max_poisson = total_number + 2 * mean_birth_number + 10
            if len(log_factorial) < max_poisson:
                for x in range(len(log_factorial), max_poisson):
                    log_x = log_factorial[x - 1] + math.log(x)
                    log_factorial.append(log_x)
            births_number = poisson(mean_birth_number, max_poisson, log_factorial)
            total_number = total_number - deaths_number + births_number
            if total_number <= 0:
                break
            mean_dependence[time_unit] += total_number / realizations_number
            dispersion_dependence[time_unit] += total_number ** 2 / realizations_number

    for time_unit in range(total_time + 1):
        dispersion_dependence[time_unit] = dispersion_dependence[time_unit] - (mean_dependence[time_unit] ** 2)
        if abs(dispersion_dependence[time_unit]) < 1e-10:
            dispersion_dependence[time_unit] = 0
        deviation_dependence[time_unit] += (math.sqrt(dispersion_dependence[time_unit] *
                                                      realizations_number / (realizations_number - 1)))
    return mean_dependence, deviation_dependence


def main():
    full_time = 100
    time_units = list(range(full_time + 1))
    cases = {'start_number': [10, 100],
             'death_coefficient': [0.01, 0.1, 1],
             'birth_coefficient': [1, 100, 1000]}
    cases_number = len(cases['death_coefficient']) * len(cases['birth_coefficient']) * len(cases['start_number'])
    case = 1
    for start in cases['start_number']:
        fig = plot.figure()
        plot.xlabel('Time')
        plot.ylabel("Hamster's number")
        for b in cases['death_coefficient']:
            for a in cases['birth_coefficient']:
                print(f'Initial hamsters number: {start}. Set of parameters: {case}/{cases_number}')
                mean, deviation = get_mean_dependence(death_coefficient=b, birth_coefficient=a, start_number=start,
                                                      realizations_number=100, total_time=full_time)
                plot.errorbar(x=time_units, y=mean, yerr=deviation, fmt='.',
                              label=f"birth_coefficient = {a}, death_coefficient = {b}")
                case = case + 1

        plot.legend()
        fig.savefig(f'result_for_{start}.svg')


if __name__ == '__main__':
    main()
