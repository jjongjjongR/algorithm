import sys
import os

input = sys.stdin.readline

def main():

    while True :
        a, b = map(int, input().strip().split())

        if a == 0 and b == 0:
            break

        print(a + b)

if __name__ == "__main__":
    main()
