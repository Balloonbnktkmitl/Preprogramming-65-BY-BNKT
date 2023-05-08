"""Prepro"""
def main():
    """37."""
    age = int(input())
    num = int(input())
    bill = 100
    if age >= 60:
        if num == 1:
            print("Free")
        else:
            print("Pay %d baht" %(bill*num*(50/100)))
    else:
        print("Pay %d baht" %(bill*num))
main()
