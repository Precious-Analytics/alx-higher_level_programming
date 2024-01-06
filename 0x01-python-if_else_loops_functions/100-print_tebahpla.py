#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    case = 'lower' if char % 2 != 0 else 'upper'
    if case == 'lower':
        print("{}".format(chr(char).upper()), end="")
    else:
        print("{}".format(chr(char)), end="")
