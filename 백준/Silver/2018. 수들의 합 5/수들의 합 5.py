import sys

def main():
    N = int(input())

    start = 1
    stop = 1

    count = 1
    sum = 1

    while stop != N:
        if sum == N:
            count += 1
            stop += 1
            sum += stop

        elif sum > N:
            sum -= start
            start += 1
        
        else:
            stop += 1
            sum += stop
    
    print(count)
        


if __name__ == "__main__":
    main()
