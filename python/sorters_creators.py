import random


def bubble_sorter(arg_list, reverse=False):
    array = arg_list.copy()
    step = 1 - int(reverse) * 2
    first = ((1 - len(array)) * step + len(array) - 1) // 2
    pos = 1
    while pos < len(array):
        is_sorted = True
        last = ((len(array) - 2 * pos + 1) * step + len(array) - 1) // 2
        for i in range(first, last, step):
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                is_sorted = False
        if is_sorted:
            break
        pos += 1
    return array


def selection_sorter(arg_list):
    array = arg_list.copy()
    for i in range(len(array)):
        index_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        array[index_min], array[i] = array[i], array[index_min]
    return array


def insertion_sorter(arg_list):
    array = arg_list.copy()
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
    return array


def shell_sorter(arg_list):
    assert len(arg_list) < 4000, 'Array is too large. Use another sorter.'
    array = arg_list.copy()

    def new_increment(arr):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
    return array


def quick_sorter(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    small_array = []
    medium_array = []
    large_array = []
    for item in array:
        if item < pivot:
            small_array.append(item)
        elif item > pivot:
            large_array.append(item)
        elif item == pivot:
            medium_array.append(item)
        else:
            raise Exception('Unexpected is happened')
    return quick_sorter(small_array) + medium_array + quick_sorter(large_array)


def merge_sorter(array, reverse=False):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left_array = merge_sorter(array[:middle])
    right_array = merge_sorter(array[middle:])
    result = []
    i = 0
    j = 0
    while i < len(left_array) or j < len(right_array):
        if j >= len(right_array) or (i < len(left_array) and left_array[i] < right_array[j]):
            if reverse:
                result.insert(0, left_array[i])
            else:
                result.append(left_array[i])
            i += 1
        else:
            if reverse:
                result.insert(0, right_array[j])
            else:
                result.append(right_array[j])
            j += 1
    return result


def reverse_array(arg_list):
    array = arg_list.copy()
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
    return array


if __name__ == '__main__':
    size = 50
    initial_array = [i for i in range(size)]
    random.shuffle(initial_array)
    print(f'\nInitial_array:\n{initial_array}')

    methods = {
        'Bubble sorter': bubble_sorter,
        'Selection sorter': selection_sorter,
        'Insertion sorter': insertion_sorter,
        'Shell sorter': shell_sorter,
        'Quick sorter': quick_sorter,
        'Merge sorter': merge_sorter,
        'Array reverser': reverse_array,
    }

    for key, value in methods.items():
        print(f'\n{key}:\n{value(initial_array)}')
