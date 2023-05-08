"""Prepro"""
def main():
    """72longsudthai"""
    round1 = 0
    min1 = 0
    min2 = 0
    dis = 0
    while round1 < 10:
        num = int(input())
        if min1 == 0:
            min1 = num
            min2 = num
            dis = num
        elif num < min1:
            tmp = min1
            min1 = num
            min2 = tmp
            dis = min2-min1
        elif num > min1:
            if num - min1 <= dis:
                min2 = num
                dis = min2-min1
        round1 += 1
    print("Almost the min :", min2)
main()
