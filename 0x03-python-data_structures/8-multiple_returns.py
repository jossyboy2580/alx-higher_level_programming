#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = None
    if len(sentence) > 0:
        first_char = sentence[0]
    return ((len(sentence), first_char))
