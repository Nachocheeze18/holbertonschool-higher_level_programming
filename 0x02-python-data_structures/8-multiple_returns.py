#!/usr/bin/python3
def multiple_returns(sentence):
    one = len(sentence)
    two = sentence[0] if sentence else None
    return (one, two)
