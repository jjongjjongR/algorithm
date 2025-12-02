import sys
import os

input = sys.stdin.readline

def main():

    n = int(input().strip())
    file_name = []
    
    for _ in range(n):
        file_name.append(input().strip())

    pattern = list(file_name[0])
    file_length = len(pattern)

    for i in range(1, n):
        current = file_name[i]
        for j in range(file_length):
            if file_name[0] == '?':
                continue
            if pattern[j] != current[j]:
                pattern[j] = '?'

    print("".join(pattern))

if __name__ == "__main__":
    main()
