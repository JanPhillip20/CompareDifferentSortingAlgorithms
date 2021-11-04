import time


def split_list(_list):
    half = len(_list) // 2
    return _list[:half], _list[half:]


def merge(left_list, right_list):
    while len(left_list) > 0 and len(right_list) > 0:
        new_list = []
        if left_list[0] <= right_list[0]:
            new_list.append(left_list[0])
            left_list.pop(0)
        else:
            new_list.append(right_list[0])
            right_list.pop(0)
    while len(left_list) > 0:
        new_list.append(left_list[0])
        left_list.pop(0)
    while len(right_list) > 0:
        new_list.append(right_list[0])
        right_list.pop(0)
    return new_list


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        left_list, right_list = split_list(unsorted_list)
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        new_list = merge(left_list, right_list)
        return new_list
