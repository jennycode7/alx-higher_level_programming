#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple of (sentence, sentence length)
    """
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
