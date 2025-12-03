import sys
import os


input = sys.stdin.readline

def main():

    a, b = map(int, input().strip().split())

    def calculater(A, B) :
        result = ( A + B ) * ( A - B )
        return print(result)

    calculater(a,b)
if __name__ == "__main__":
    main()
