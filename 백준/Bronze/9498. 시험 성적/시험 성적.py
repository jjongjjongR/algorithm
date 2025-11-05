import sys
import os

input = sys.stdin.readline

def main():

    num = int(input().strip())

    if(num >= 90):
        print("A")
    elif(num >= 80):
        print("B")
    elif(num >= 70):
        print("C")
    elif(num >= 60):
        print("D")
    else:
        print("F")

if __name__ == "__main__":
    main()
