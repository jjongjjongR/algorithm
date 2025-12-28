import sys
import os

input = sys.stdin.readline

def main():

    t = int(input())

    for _ in range(t):
        r, s = input().split()
        r = int(r)

        result = ''

        for i in s:
            result = result + ( i * r )

        print(result)

if __name__ == "__main__":
    main()
