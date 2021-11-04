import time
from BinaryTreeSort.BinaryTreeSort_Node import BinaryTreeSort_Node


def run_binary_tree_sort(unsorted_list):

    bts = BinaryTreeSort_Node()
    t0 = time.time()
    for num in unsorted_list:
        bts.insert(num)
    sortedlist = bts.inorder([])

    t1 = time.time()
    return t1-t0, sortedlist


