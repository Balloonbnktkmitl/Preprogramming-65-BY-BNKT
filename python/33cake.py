"""Prepro"""
def main():
    """33."""
    money = int(input())
    cakebill = int(input())
    numcake = money//cakebill
    moneylf = money-(cakebill*numcake)
    if numcake > 0:
        print("Chocolate Cake: %d" %numcake)
        print("Money left: %d" %moneylf)
    else:
        print("Not enough money;(")
        print("Money left: %d" %money)
main()
