import sys

input = sys.stdin.readline

def main():
# 3 4 1 2 5

    num_count, reverse_count = map(int, input().strip().split())

    nums = [ _ for _ in range(1, num_count+1)]

    for _ in range(reverse_count):
        i, j = map(int, input().split())

        left = i-1
        right = j-1

        while(left < right):
            _right = nums[right]
            nums[right] = nums[left]
            nums[left] = _right
            right -= 1
            left += 1

    for index in nums:
        print(index, end=' ')

    
if __name__ == "__main__":
    main()