#!/usr/bin/env python
"""This script prompts a user to enter a message to encode or decode
 3  using a classic Caeser shift substitution (3 letter shift)
 """

from typing import Sequence


def bubble_sort(my_iterable: Sequence) -> Sequence:
    """
    Buble sort: Sorts using bubble sort method https://en.wikipedia.org/wiki/Bubble_sort
    args:
        my_iterable: takes any iterable with len method eg list or tuples
    returns:
        my_iterable: returns the iterable

    """
    for i in range(len(my_iterable), -1, -1):
        for j in range(1, i):
            if my_iterable[j - 1] > my_iterable[j]:
                temp = my_iterable[j - 1]
                my_iterable[j - 1] = my_iterable[j]
                my_iterable[j] = temp

    return my_iterable


def insert_sort(my_iterable: Sequence) -> Sequence:
    """
    Insert sort: Sorts using insert sort method
    args:
        my_iterable: takes any iterable with len method eg list or tuples
    returns:
        my_iterable: returns the iterable

    """
    for i in range(1, len(my_iterable)):
        value = my_iterable[i]
        j = i - 1
        while j >= 0 and (my_iterable[j] > value):
            # shift the value to left
            my_iterable[j + 1] = my_iterable[j]
            j = j - 1
        # finally assign the value to its place
        my_iterable[j + 1] = value
    return my_iterable


def merge_sort(my_iterable: Sequence) -> Sequence:
    """
    Merge sort: Sort using merge sort
    args:
        my_iterable: takes any iterable with len method eg list or tuple
    returns:
        sorted list
    """
    if len(my_iterable) <= 1:
        return my_iterable
    # Fin the middle point and devide it
    middle = len(my_iterable) // 2
    left_list = my_iterable[:middle]
    right_list = my_iterable[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))


def merge(lef_half: Sequence, right_half: Sequence) -> list:
    """
    Merge: merges and sorts the two half of a list
    args:
        left_half: list first half of list
        right_half: right half of a list
    return:
        res: merged and sorted list of left & right half
    """
    res = []
    while len(lef_half) != 0 and len(right_half) != 0:
        if lef_half[0] < right_half[0]:
            res.append(right_half[0])
            lef_half.remove(lef_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(lef_half) == 0:
        res = res + right_half
    else:
        res = res + lef_half
    return res
