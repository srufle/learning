#!/bin/python3

# C:\code\grokking_algorithms_rufle\grokking_examples10.py
import operator
import random
from collections import deque
import math

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
        less = [ele for ele in array[1:] if less_op(ele[1]['distance'], pivot[1]['distance'])]
        greater = [ele for ele in array[1:] if greater_op(ele[1]['distance'], pivot[1]['distance'])]

        return my_qsort(less, direction) + [pivot] + my_qsort(greater, direction)

def main():
    # [weather, weekend, game_is_on]
    A = [5, 1, 0]
    B = [3, 1, 1]
    C = [1, 1, 0]
    D = [4, 0, 1]
    E = [4, 0, 0]
    F = [2, 0, 0]
    data = {
        "A": {"values": A, "total_loves": 300},
        "B": {"values": B, "total_loves": 225},
        "C": {"values": C, "total_loves": 75},
        "D": {"values": D, "total_loves": 200},
        "E": {"values": E, "total_loves": 150},
        "F": {"values": F, "total_loves": 50}
            }
    target = [4, 1, 0]
    distances = {}
    for key in data.keys():
        values = data[key]["values"]
        x = 0
        acum = 0
        for index in range(3):
            x = target[index] - values[index]
            #print(f"x = {target[index]} - {values[index]} = {x}")
            xx = math.pow(x, 2)
            #print(f"xx = math.pow({x}, 2) = {xx}")
            acum += xx
            #print(f"acum = {acum}")

        result = math.sqrt(acum)
        distances[key] = {"distance": result}
        print(f"Distance of {key} to target = '{result:{4}.{6}}'")

    neighbors = 4
    al = list(distances.items())
    al = my_qsort(al, "asc")
    loaves_to_bake = 0
    for item in al[:neighbors]:
        loaves_to_bake += data[item[0]]["total_loves"]
    loaves_to_bake = loaves_to_bake/neighbors

    print(f"closest neighbors sorted ascending = {distances}")
    print(f"loaves to bake today = {loaves_to_bake}")

main()
