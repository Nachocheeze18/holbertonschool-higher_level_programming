#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = a / b
        str = '{}'.format(x)
    except ZeroDivisionError:
        str = 'None'
    finally:
        print('Inside result: {}'.format(str))
    return str
