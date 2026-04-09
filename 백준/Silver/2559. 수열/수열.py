import sys

input = sys.stdin.readline

num_list = []
now_list = []
sum_num = 0
max_num = 0

def num_add(c):
    global num_list, sum_num, K
    sum_num += num_list[c+K]


def num_remove(c):
    global num_list, sum_num, K
    sum_num -= num_list[c]



def main():
# 21
    global num_list, max_num, sum_num, K

    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(K):
        sum_num += num_list[i]
        max_num += num_list[i]

    for i in range(N - K):
        num_add(i)
        num_remove(i)

        if sum_num > max_num:
            max_num = sum_num

    print(max_num)

if __name__ == "__main__":
    main()