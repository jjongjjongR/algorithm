import sys
import os

input = sys.stdin.readline

def main():

    size = []

    n = int(input().strip())
    size = list(input().strip().split())
    t, p = map(int, input().strip().split())
    result = 0

    for i in size:
        X = int(i)

        if X == 0:
            packs = 0
        else:
            packs = X // t
            
            if X % t != 0:
                packs += 1
        
        result += packs

    pen = n//p
    pen_remain = n - p*pen

    print(result)
    print(pen, pen_remain)

if __name__ == "__main__":
    main()
