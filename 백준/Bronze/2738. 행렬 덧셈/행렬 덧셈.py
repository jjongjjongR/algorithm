import sys
import os

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    A = []
    B = []

    for _ in range(n):
        layer = []
        numbers = input().split()
        for num in numbers:
            layer.append(int(num))
        A.append(layer)

    # print(A)

    for _ in range(n):
        layer = []
        numbers = input().split()
        for num in numbers:
            layer.append(int(num))
        B.append(layer)
    
    # print(B)

    for i in range(n):
        for j in range(m):
            print(A[i][j] + B[i][j], end=' ')
        print() 

if __name__ == "__main__":
    main()
