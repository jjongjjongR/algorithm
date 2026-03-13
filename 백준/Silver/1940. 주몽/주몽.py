import sys

def main():
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    # print(A)

    A.sort()

    count = 0
    sum = 0
    start = 0
    stop = N-1

    while start != stop:
        sum = A[start] + A[stop]

        if sum == M:
            count += 1
            start += 1
        elif sum < M:
            start += 1
        else :
            stop -= 1
    
    print(count)

if __name__ == "__main__":
    main()
