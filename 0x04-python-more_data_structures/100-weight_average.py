#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    res = 0
    total_weight = 0

    for score, weight in my_list:
        res += (score * weight)
        total_weight += weight
    return (res/total_weight)
