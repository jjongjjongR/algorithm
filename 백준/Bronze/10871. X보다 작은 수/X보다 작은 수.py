import sys
import os

input = sys.stdin.readline

def main():
    N, X = map(int, input().strip().split())
    num = list(map(int, input().strip().split()))
    
    result = []

    for nume in num:
        if(nume < X):
           result.append(str(nume))

    print(' '.join(result))

if __name__ == "__main__":
    main()
