"""Prepro"""
def main():
    """25"""
    number = int(input())
    num1 = str(int((number/100000000))%10)
    num2 = str(int((number/1000000))%10)
    num3 = str(int((number/10000))%10)
    num4 = str(int((number/100))%10)
    num5 = str((number)%10)
    print(num1+num2+num3+num4+num5)
main()
