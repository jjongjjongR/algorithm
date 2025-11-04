import sys
import os

input = sys.stdin.readline

def main():

    while(True):
        M, F = map(int, input().strip().split())
        if(M == 0 and F==0):
            break            
        print(M+F)

if __name__ == "__main__":
    main()
