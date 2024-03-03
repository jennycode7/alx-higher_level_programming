#!/usr/bin/python3
"""
A module
"""


def text_indentation(text):
    """
    adds an indentation to the text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', ':', '?']
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in punctuation:
            print('\n' * 2, end='')
            if i < len(text) - 1 and text[i + 1] == ' ':
                i += 1
        i += 1
