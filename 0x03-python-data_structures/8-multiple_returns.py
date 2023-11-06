#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence.append(None)
    return len(sentence), sentence[0]
