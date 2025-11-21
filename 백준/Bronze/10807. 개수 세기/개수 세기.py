import sys
import os

input = sys.stdin.readline

def main():

    n = int(input().strip())
    m= list(map(int, input().strip().split()))
    v = int(input().strip())
    
    result = 0

    for i in range(n):
        if(m[i] == v):
            result+=1

    print(result)
    
if __name__ == "__main__":
    main()
