import sys
import os

input = sys.stdin.readline

def main():
    k, d, a = map(int, input().split('/'))
    
    if d == 0 or k+a < d:
        print("hasu")
    else:
        print("gosu")

if __name__ == "__main__":
    main()
