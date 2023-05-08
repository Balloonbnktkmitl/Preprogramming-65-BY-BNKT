"""Prepro"""
def yonum(num1, num2, num3, num4, num5):
    '''Max statement'''
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        print('''MAX : %d''' %num1)
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        print('''MAX : %d''' %num2)
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        print('''MAX : %d''' %num3)
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        print('''MAX : %d''' %num4)
    elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
        print('''MAX : %d''' %num5)
def nonum(num1, num2, num3, num4, num5):
    '''Min statement'''
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5:
        print('''MIN : %d''' %num1)
    elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
        print('''MIN : %d''' %num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
        print('''MIN : %d''' %num3)
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5:
        print('''MIN : %d''' %num4)
    elif num5 <= num1 and num5 <= num2 and num5 <= num3 and num5 <= num4:
        print('''MIN : %d''' %num5)
def main():
    """57.I'm Max & I'm Min"""
    typ = input().upper()
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if typ == '''MAX''':
        yonum(num1, num2, num3, num4, num5)
    else:
        nonum(num1, num2, num3, num4, num5)
main()
