"""Prepro"""
def main():
    """31.taobin"""
    money = float(input())
    water = float(input())
    cal = money-water
    maxmon25 = cal/0.25
    min10 = cal//10
    cal2 = cal%10
    min5 = cal2//5
    cal3 = cal2%5
    min2 = cal3//2
    min1 = cal2%2
    cal4 = cal%1
    min50 = cal4//0.5
    cal5 = cal4%0.5
    min25 = cal5//0.25
    print(int(maxmon25))
    print(int(min10+min5+min2+min1+min25+min50))
    print(cal)
main()
