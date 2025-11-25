import sys
import os

input = sys.stdin.readline

def main():
    line = int(input())

    for i in range(line):
        name = input().rstrip('\n')
        print(f"{i+1}. {name}")
#        print(len(name))


if __name__ == "__main__":
    main()
