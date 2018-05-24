#!/bin/python3

# C:\code\grokking_algorithms_rufle\grokking_examples01.py
import operator
import random
from collections import deque

def find_best_land_plot(length, width):
    longest = max(length, width)
    shortest = min(length, width)
    result = longest % shortest
    if result == 0:
        return shortest
    else:
        return find_best_land_plot(shortest, result)


def sum_list(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_list(array[1:])


def my_max_list(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        first = array[0]
        second = my_max_list(array[1:])
        if first < second:
            return second
        elif first > second:
            return first


def my_qsort(array, direction=None):
    less_op = operator.le
    greater_op = operator.gt
    if direction == "desc":
        less_op = operator.gt
        greater_op = operator.le

    if len(array) < 2:
        return array
    else:
        index = min(0, (len(array) // 2))
        pivot = array[index]
        # pivot = array[0]

        # ++ Long Way
        # less = []
        # for ele in array[1:]:
        #     if less_op(ele, pivot):
        #         less += [ele]

        # ++ Long Way
        # greater = []
        # for ele in array[1:]:
        #     if greater_op(ele, pivot):
        #         greater += [ele]

        # ++ Short Way
        less = [ele for ele in array[1:] if less_op(ele, pivot)]
        greater = [ele for ele in array[1:] if greater_op(ele, pivot)]

        return my_qsort(less, direction) + [pivot] + my_qsort(greater, direction)

def main():
    print("Find common area")
    length = 1680
    width = 640
    best_size = find_best_land_plot(length, width)
    print(f"Best fit {best_size} common area")

    some_list = [2, 4, 6]
    total = sum_list(some_list)
    print(f"Total sum of '{some_list}' is '{total}'")

    some_list = []
    my_max = my_max_list(some_list)
    print(f"Max of '{some_list}' is '{my_max}'")

    some_list = [2]
    my_max = my_max_list(some_list)
    print(f"Max of '{some_list}' is '{my_max}'")

    some_list = [2, 4, 6]
    my_max = my_max_list(some_list)
    print(f"Max of '{some_list}' is '{my_max}'")

    some_list = [9, 4, 10]
    my_max = my_max_list(some_list)
    print(f"Max of '{some_list}' is '{my_max}'")

    some_list = [11, 4, 3]
    my_max = my_max_list(some_list)
    print(f"Max of '{some_list}' is '{my_max}'")

    some_list = [11, 4, 3]
    sorted_list = my_qsort(some_list, "asc")
    print(f"Sorting of '{some_list}' is '{sorted_list}'")

    some_list = [2, 4, 6]
    sorted_list = my_qsort(some_list, "desc")
    print(f"Sorting of '{some_list}' is '{sorted_list}'")

    max_value = 6
    some_list = random.sample(range(1, max_value), (max_value-1))
    sorted_list = my_qsort(some_list, "asc")
    print(f"Sorting of '{some_list}' is '{sorted_list}'")

    max_value = 6
    some_list = random.sample(range(1, max_value), (max_value-1))
    some_list += some_list
    sorted_list = my_qsort(some_list, "asc")
    print(f"Sorting of '{some_list}' is '{sorted_list}'")

main()
