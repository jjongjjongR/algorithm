import sys
import os

input = sys.stdin.readline

def main():

    line = input().strip()

    if 1 <= int(line) <= 9:
        print(1)
        return
    
    found = False
    for a in range(2, 10):
        for b in range(1, 10):
            if a * b == int(line):
                found = True
                break
        if found:
            break

    if found:
        print(1)
    else:
        print(0)



if __name__ == "__main__":
    main()
