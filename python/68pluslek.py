"""Prepro"""
def main():
    """68"""
    sum1 = 0
    for i in range(10):
        i = i
        num = int(input())
        if num < 0:
            sum1 = sum1 + -5
        else:
            sum1 = sum1 + num
    if sum1 < 0:
        print(-5)
    else:
        print(sum1)
main()
