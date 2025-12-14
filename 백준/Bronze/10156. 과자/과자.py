import sys
import os

input = sys.stdin.readline

def main():

    k, n, m = map(int, input().split())

    total = k * n

    if total > m:
        print(total - m)
    else:
        print(0)

if __name__ == "__main__":
    main()
