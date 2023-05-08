"""Prepro"""
import math

def main():
    """49."""
    numn = int(input())
    numr = int(input())
    cal = (math.factorial(numn))/((math.factorial(numr))*(math.factorial(numn-numr)))
    print(int(cal))
main()
