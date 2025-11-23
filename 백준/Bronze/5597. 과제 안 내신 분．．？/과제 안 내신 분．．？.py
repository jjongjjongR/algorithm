import sys
import os

input = sys.stdin.readline

def main():
    list_s = [0] * 31 
    count = 0

    for _ in range(28):
        n = int(input())
            
        list_s[n] = 1 


    for i in range(1, 31):

        if list_s[i] == 0:

            print(i)
            count += 1

        if count == 2:
            break


if __name__ == "__main__":
    main()
