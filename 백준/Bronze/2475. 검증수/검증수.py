import sys
import os

input = sys.stdin.readline

def main():

    nums = list(map(int, input().split()))
    checksum = sum(x * x for x in nums) % 10
    
    print(checksum)

if __name__ == "__main__":
    main()
