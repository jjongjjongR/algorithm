import sys
import os

input = sys.stdin.readline

def main():

    lv, judgment = input().split()
    score = 0
    lv = int(lv)

    if judgment == "miss":
        score = 0
    elif judgment == "bad":
        score = 200 * lv
    elif judgment == "cool":
        score = 400 * lv
    elif judgment == "great":
        score = 600 * lv
    elif judgment == "perfect":
        score = 1000 * lv

    print(score)

if __name__ == "__main__":
    main()
