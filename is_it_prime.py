def is_it_prime(numerator):
    if type(numerator) != int or numerator < 1:
        print('Error in function call.')
    else:
        count = 0
        for denominator in range(1, numerator + 1):
            if numerator % denominator == 0:
                count += 1

        if count != 2:
            return False

        return True


if __name__ == '__main__':
    for number in range(1, 100):
        if is_it_prime(number):
            print(number)
