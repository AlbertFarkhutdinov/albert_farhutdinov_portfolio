import random


def bubble_sort(array, reverse=False):
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


def selection_sort(array):
    for i in range(len(array)):
        index_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        array[index_min], array[i] = array[i], array[index_min]


def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam


def shell_sort(array):
    assert len(array) < 4000, 'Array is too large. Use another sorter.'

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


def quick_sort(array, first, last):
    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i, j = first, last
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort(array, first, j)
    quick_sort(array, i, last)


def reverse_array(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]


if __name__ == '__main__':
    size = 50
    initial_array = [i for i in range(size)]
    random.shuffle(initial_array)

    print(f'\nInitial_array:\n{initial_array}')
    methods = {
        'Bubble sorter': bubble_sort,
        'Selection sorter': selection_sort,
        'Insertion sorter': insertion_sort,
        'Shell sorter': shell_sort,
        'Quick sorter': quick_sort,
        'Array reverser': reverse_array,
    }

    for key, value in methods.items():
        new_array = initial_array[:]
        if key == 'Quick sorter':
            value(new_array, 0, size - 1)
        else:
            value(new_array)
        print(f'\n{key}:\n{new_array}')
