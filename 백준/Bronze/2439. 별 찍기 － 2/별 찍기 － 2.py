import sys
import os

input = sys.stdin.readline

def main():

    N = int(input().strip())

    for i in range(1, N+1, 1):
        for _ in range(0, N-i, 1):
            print(" ", end='')
        print("*"*i)

          

if __name__ == "__main__":
    main()
