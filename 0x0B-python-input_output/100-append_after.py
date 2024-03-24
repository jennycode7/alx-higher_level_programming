#!/usr/bin/python3
"""
A module
"""

def search_word_in_string(word, string):
    """
    search word
    """
    return word in string

def append_after(filename="", search_string="", new_string=""):
    """
    appends after
    """
    with open(filename, "r") as file:
        string = file.readlines()
        for line in string:
            if search_word_in_string(search_string, line):
                string.insert(string.index(line) + 1, new_string)

    with open(filename, "w") as file:
        file.writelines(string)
