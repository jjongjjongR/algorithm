import sys
import os
from collections import deque

input = sys.stdin.readline

def main():

    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, L, A)

    mydeque = deque()

    for i in range(N):
        while mydeque and mydeque[-1][0] > A[i]:
            mydeque.pop()
        mydeque.append((A[i],i))
        
        if mydeque[0][1] <= i-L:
            mydeque.popleft()

        print(mydeque[0][0], end=' ')


if __name__ == "__main__":
    main()
