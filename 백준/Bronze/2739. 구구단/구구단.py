import sys
import os

input = sys.stdin.readline

def main():
    N = int(input().strip())

    for nume in range(1,10,1):
        result = N * nume
        print(f'{N} * {nume} = {result}')

if __name__ == "__main__":
    main()
