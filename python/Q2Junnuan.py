"""Quiz"""
import math
def main():
    """Jumnuanchapoo"""
    num = int(input())
    tmp = 2
    ans = True
    if num > 1:
        while tmp <= math.sqrt(num):
            if num % tmp < 1:
                ans = False
            tmp = tmp + 1
    else:
        ans = False
    if ans:
        print("Prime Number")
    else:
        print("Not Prime Number")
main()
