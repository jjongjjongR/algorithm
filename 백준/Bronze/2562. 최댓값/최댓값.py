import sys
import os

input = sys.stdin.readline

def main():

    numbers = []

    for _ in range(9):
        numbers.append(int(input()))

    value = max(numbers)
    index = numbers.index(value) + 1

    print(value)
    print(index)

if __name__ == "__main__":
    main()
