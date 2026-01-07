import sys
import os

input = sys.stdin.readline

def main():

    n = int(input().strip())

    sell_book = dict()

    for _ in range(n):
        book_name = input().strip()
        
        if book_name in sell_book:
            sell_book[book_name] += 1
        else:
            sell_book[book_name] = 1
    
    best_title = ""
    best_count = 0

    for book_title, i in sell_book.items():
        if i > best_count:
            best_title = book_title
            best_count = i
        elif i == best_count:
            if book_title < best_title:
                best_title = book_title 

    print(best_title)
    



if __name__ == "__main__":
    main()
