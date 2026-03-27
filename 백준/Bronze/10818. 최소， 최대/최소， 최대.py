import sys

input = sys.stdin.readline

def main():
    N = int(input().strip())
    num_list = list(map(int, input().strip().split()))

    min = num_list[0]
    max = num_list[0]

    for index in range(N):
        now_num = num_list[index]

        if now_num > max:
            max = now_num

        if now_num < min:
            min = now_num

    print(min, max)

if __name__ == "__main__":
    main()