"""Prepro"""
def main():
    """71sarub"""
    roundend = int(input())
    rounds = 0
    posia = 1
    posib = 2
    posic = 3
    while rounds < roundend:
        sarub = input()
        if sarub == "12" or sarub == "21":
            typ = posia
            posia = posib
            posib = typ
        elif sarub == "13" or sarub == "31":
            typ = posia
            posia = posic
            posic = typ
        elif sarub == "23" or sarub == "32":
            typ = posib
            posib = posic
            posic = typ
        rounds += 1
    if posia == 1 and posib == 2 and posic == 3:
        print("A")
        print("B")
        print("C")
    elif posia == 1 and posib == 3 and posic == 2:
        print("A")
        print("C")
        print("B")
    elif posia == 2 and posib == 1 and posic == 3:
        print("B")
        print("A")
        print("C")
    elif posia == 2 and posib == 3 and posic == 1:
        print("B")
        print("C")
        print("A")
    elif posia == 3 and posib == 1 and posic == 2:
        print("C")
        print("A")
        print("B")
    elif posia == 3 and posib == 2 and posic == 1:
        print("C")
        print("B")
        print("A")
main()
