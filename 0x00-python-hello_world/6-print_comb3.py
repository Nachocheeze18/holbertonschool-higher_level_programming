#!/usr/bin/python3
x = 1
for i in range(0, 10):
    for x in range(i+1, 10):
        if (i != 8):
            print("{one}{two}, ".format(one=i, two=x), end='')
        elif (i == 8):
            print("{one}{two}".format(one=i, two=x))
    x = x + 1
