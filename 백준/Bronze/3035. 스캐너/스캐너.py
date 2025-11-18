import sys
import os

input = sys.stdin.readline

def main():

    r, c, zr, zc = map(int, input().strip().split())
    news=[]
    result = []
    for _ in range(r):
        news.append(list(input().strip()))
    #print(news)

    for i in range(r):
        layer=[]
        for j in range(c):
            layer.append(news[i][j]*zc)
        
        for _ in range(zr):
            result.append(layer)
    #print(result)
    
    for rzr in range(r*zr):
        for czc in range(c):
            print(result[rzr][czc], end="")
        print("")

if __name__ == "__main__":
    main()
