import sys
import os

input = sys.stdin.readline

def main():

    a, p, c = map(int, input().split())

    print(max(a + c, p))

if __name__ == "__main__":
    main()
