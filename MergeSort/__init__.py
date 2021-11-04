import time
from MergeSort.Merge_Sort import merge_sort


def run_merge_sort(unsorted_list):
    t0 = time.time()
    merge_sort(unsorted_list)
    t1 = time.time()
    return t1-t0, unsorted_list
