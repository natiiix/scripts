#!/bin/python3

from sys import argv

if __name__ == '__main__':
    text = argv[1] if len(argv) == 2 else input('Enter an ASCII string: ')

    lastChar = 0
    for c in text:
        cOrd = ord(c)
        diff = cOrd - lastChar
        lastChar = cOrd

        if diff > 0:
            print(diff * '+', end='')
        elif diff < 0:
            print(-diff * '-', end='')

        print('.', end='')

    print()
