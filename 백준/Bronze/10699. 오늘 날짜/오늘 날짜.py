import datetime
import sys
import os

def main():

    now = datetime.datetime.now()
    time_d = datetime.timedelta(hours=9)
    kst = now + time_d

    year = kst.year
    month = kst.month
    day = kst.day

    print(f"{year}-{month}-0{day}")

if __name__ == "__main__":
    main()
