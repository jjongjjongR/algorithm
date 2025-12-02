import sys
import os

input = sys.stdin.readline

def main():

    n = int(input().strip())
    count = 0

    for i in range(1, n+1):
        str_i = str(i)

        for j in str_i:
            if j in '369':
                count += 1

    print(count)

if __name__ == "__main__":
    main()
