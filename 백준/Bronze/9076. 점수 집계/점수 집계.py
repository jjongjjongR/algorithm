import sys
import os

input = sys.stdin.readline

def main():
    count = int(input())

    for i in range(count):
        num = list(map(int, input().split()))
        
        maxnum = max(num)
        minnum = min(num)

        num.remove(maxnum)
        num.remove(minnum)

        maxnum2 = max(num)
        minnum2 = min(num)

        if(maxnum2 - minnum2 >= 4):
            print("KIN")
        else:
            print(sum(num))


if __name__ == "__main__":
    main()
