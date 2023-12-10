#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the element at the given index.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list  
    for x in my_list:
        if x == my_list[idx]:
            my_list.remove(x)
            return my_list
