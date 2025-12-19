import sys
import os

input = sys.stdin.readline

def main():

    a = input().strip()
    b = input().strip()
    c = input().strip()

    num = int(a) + int(b) - int(c)
    print(num)

    str = int(a + b) - int(c)
    print(str)

if __name__ == "__main__":
    main()
