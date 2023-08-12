#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    def find_item(b):
        if my_list[idx] == b:
            return b
        else:
            return 0
    found = sum(list(map(find_item, my_list)))
    return (found)
