#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    print('{one} + {two} = {results}'.format(one=a, two=b, results=add(a, b)))
