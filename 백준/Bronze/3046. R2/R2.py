import sys
import os

input = sys.stdin.readline

def main():
    r1, s = map(int, input().split())
    r2 = 2 * s - r1  

    print(r2)

if __name__ == "__main__":
    main()
