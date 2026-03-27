import sys

input = sys.stdin.readline

def main():

    nums = [0] * 9

    for i in range(9):
        nums[i] = int(input().strip())

    max = nums[0]
    max_index = 1

    for index in range(9):
        now_num = nums[index]

        if now_num > max:
            max = now_num
            max_index = index + 1

    print(max, max_index)

if __name__ == "__main__":
    main()