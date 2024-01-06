#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    case = 'lower' if char % 2 != 0 else 'upper'
    print(
            "{}".format(chr(char).upper() if case == 'lower' else chr(char)), 
            end=""
            )
