#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    NewList = []
    for i in range((len(my_list))):
        if idx == i:
            NewList.append(element)
        else:
            NewList.append(my_list[i])
    return NewList
