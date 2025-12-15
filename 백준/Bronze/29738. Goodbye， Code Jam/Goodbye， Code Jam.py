import sys
import os

input = sys.stdin.readline

def main():

    t = int(input().strip())

    for i in range(1, t + 1):
        N = int(input().strip())
        
        if N > 4500:
            result = "Round 1"
        elif N > 1000:
            result = "Round 2"
        elif N > 25:
            result = "Round 3"
        else:
            result = "World Finals"
        
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()
