from BinaryTreeSort import run_binary_tree_sort
from BubbleSort.Bubble_Sort import bubble_sort_integer
from InsertionSort.Insertion_Sort import insertion_sort_integer
from MergeSort import run_merge_sort
from TestValues.Random_Integers import get_random_numbers_by_given_length
from TestValues.Random_Strings import create_string_list
# Mergesort
# Quicksort (nicht stabil)
# Heapsort (nicht stabil)


def run_sorting_algorithms(list):
    time_of_insertion_sort, sorted_list_with_insertion_sort = insertion_sort_integer(list) # fehler
    print("Time insertion sort: ", time_of_insertion_sort)
    print(sorted_list_with_insertion_sort)

    time_of_binary_tree_sort, sorted_list_with_binary_tree_sort = run_binary_tree_sort(list)
    print("Time binary tree sort: ", time_of_binary_tree_sort)
    print(sorted_list_with_binary_tree_sort)

    time_of_bubble_sort, sorted_list_with_bubble_sort = bubble_sort_integer(list)
    print("Time bubble sort: ", time_of_bubble_sort)
    print(sorted_list_with_bubble_sort)

    time_of_merge_sort, sorted_list_with_merge_sort = run_merge_sort(list)
    print("Time merge sort: ", time_of_merge_sort)
    print(sorted_list_with_merge_sort)


if __name__ == '__main__':
    print("Compare different sorting algorithms")

    flag = 0
    while flag == 0:
        _input = input("Do you want to run the sort alg. with numbers oder strings? Enter n for numbers, s for strings!")
        if _input == "n" or _input == "N":
            length = int(input("Enter the length of list:"))
            run_sorting_algorithms(get_random_numbers_by_given_length(length))
            flag = 1
        elif _input == "s" or _input == "S":
            run_sorting_algorithms(create_string_list())
            flag = 1
        else:
            print("No valid input")

    #input("Press enter to exit!")
