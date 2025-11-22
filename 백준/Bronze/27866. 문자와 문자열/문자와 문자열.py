import sys
import os

input = sys.stdin.readline

def main():

    s = list(input())
    i = int(input().strip())

    print(s[i-1])
    
if __name__ == "__main__":
    main()
