import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, A)

    count = 0

    for i in range(N):
        start = 0
        stop = N-1
        target = A[i]
        while start < stop:
            if A[start] + A[stop] == target:
                if start != i and stop !=i:
                    count += 1 
                    break
                elif start == i:
                    start += 1
                else:
                    stop -=1
            elif A[start] + A[stop] < target:
                start += 1
            else:
                stop -= 1

    print(count)

if __name__ == "__main__":
    main()
