import sys
import os
import math

input = sys.stdin.readline

def main():

    N, M = map(int, input().split())
    A = []
    S = [0] * N
    R = [0] * N # 나머지 표
    result = 0 # 총 갯수

    A = (list(map(int, input().split()))) # 입력된 배열

    for i in range(N):
        S[i] = S[i-1] + A[i]

    for i in range(N):
        if S[i] % M == 0:
            result += 1
        R[i] = S[i] % M

    # 나머지 값(인덱스) 갯수 표를 만들거임.
    count = [0] * M

    for i in range(N):
        index = R[i]  
        count[index] += 1
        # print(index)

    # 인덱스 개수가 2 이상이면, 구간 합의 나머지는 0이다.
    # 따라서 조건문으로 2개 이상인 것을 찾아 카운트 올리기
    # 근데 조합으로 올려야함.
    for i in range(M):
        if count[i] > 1 :
            result += math.comb(count[i],2)

    print(result)

if __name__ == "__main__":
    main()
