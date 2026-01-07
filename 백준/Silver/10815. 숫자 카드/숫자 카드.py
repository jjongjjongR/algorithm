import sys
import os

input = sys.stdin.readline

def main():

    n = int(input().strip())
    num_1 = set(input().strip().split())

    m = input().strip()
    num_2 = list(input().strip().split())

    result = []

    for i in num_2:
        if i in num_1:
            result.append("1")
        else:
            result.append("0")

    print(" ".join(result))


if __name__ == "__main__":
    main()
