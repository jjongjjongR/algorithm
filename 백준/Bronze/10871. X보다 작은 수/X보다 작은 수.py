import sys
import os

input = sys.stdin.readline

def main():
    N, X = map(int, input().strip().split())
    li = list(map(int, input().strip().split()))
    fin_li = li[:N]

    for li_num in fin_li:
        if (li_num < X):
            print(li_num, end=' ')
if __name__ == "__main__":
    main()
