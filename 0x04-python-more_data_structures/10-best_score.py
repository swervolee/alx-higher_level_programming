#!/usr/bin/python3
from functools import reduce

def best_score(dct):
    if dct is None:
        return (None)
    best = reduce(lambda a, b:a if dct[a] > dct[b] else b, dct)
    return (best)
