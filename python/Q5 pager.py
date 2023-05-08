"""Quiz"""
def main():
    """Q5 pager"""
    word = input()
    money = 0
    print("Text's length is : \"%d\"" %(len(word)))
    word1 = len(word)
    while word1 > 0:
        if word1 >= 20:
            money += 18.5
            word1 -= 20
        elif word1 >= 8:
            money += 6.5
            word1 -= 8
        elif word1 >= 3:
            money += 3
            word1 -= 3
        elif word1 >= 1:
            money += 1.5
            word1 -= 1
    print("Total price is   : %.2f Baht\.-" %(money))
main()
