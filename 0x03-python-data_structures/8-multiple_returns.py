#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if (length == 0):
        tp = (length, None)
    else:
        tp = (length, sentence[0])

    return (tp)
