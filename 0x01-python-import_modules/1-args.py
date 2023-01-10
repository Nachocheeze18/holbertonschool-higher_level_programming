#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    amount = len(sys.argv)

if (amount == 1):
    print('{} arguments.'.format(amount-1))
elif (amount == 2):
    print('{} argument:'.format(amount-1))
else:
    print('{} arguments:'.format(amount-1))

if (amount == 0):
    print('{}: {}'.format(0, sys.argv[0]))

for i in range(1, amount):
    val = sys.argv[i]
    print('{}: {}'.format(i, val))
