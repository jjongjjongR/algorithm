import sys
import os

input = sys.stdin.readline

def main():

    text = input().strip()

    if text == "":
        print(0)
    else:
        print(len(text.split()))

if __name__ == "__main__":
    main()
