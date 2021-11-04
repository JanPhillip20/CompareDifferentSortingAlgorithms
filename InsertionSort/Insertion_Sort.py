import time


def insertion_sort_integer(unsorted_list_of_integers):

    t0 = time.time()
    for i in range(1, len(unsorted_list_of_integers)):
        temp_insertion_value = unsorted_list_of_integers[i]
        j = i - 1
        while (j >= 0) and (unsorted_list_of_integers[j] > temp_insertion_value):
            unsorted_list_of_integers[j+1] = unsorted_list_of_integers[j]
            j -= 1
        unsorted_list_of_integers[j+1] = temp_insertion_value
    t1 = time.time()

    return t1 - t0, unsorted_list_of_integers


