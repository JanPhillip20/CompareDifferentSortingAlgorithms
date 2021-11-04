import time


def bubble_sort_integer(unsorted_list_of_integers):
    length = len(unsorted_list_of_integers)
    t0 = time.time()
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if unsorted_list_of_integers[j] > unsorted_list_of_integers[j + 1]:
                unsorted_list_of_integers[j], unsorted_list_of_integers[j + 1] = unsorted_list_of_integers[j + 1], \
                                                                                 unsorted_list_of_integers[j]
    t1 = time.time()
    total_time = t1 - t0
    return total_time, unsorted_list_of_integers


class Bubble_sort:
    pass
