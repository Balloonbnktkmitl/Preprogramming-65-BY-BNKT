"""Prepro"""
import math
def main():
    """91Walking average distance"""
    day = int(input())
    walklist = []
    sumwalk = 0
    for i in range(day):
        walklist.append(int(input()))
        sumwalk += walklist[i]
    avg = sumwalk/day
    for i in range(day):
        print(math.ceil(abs(walklist[i]-avg)))
main()
