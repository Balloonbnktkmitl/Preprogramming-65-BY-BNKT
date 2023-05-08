"""Prepro"""
def main():
    """36."""
    job = input()
    if job == "Magician":
        guild = input()
        num = int(input())
        if guild == "Fairy Tail":
            print("Total %d Jewel" %((num*12800)*(80/100))) 
        elif guild == "Sabertooth" and num > 5:
            print("Total %d Jewel" %((num*12800)*(85/100)))
        elif guild == "Lamia Scale" and num >= 3:
            print("Total %d Jewel" %((num*12800)*(90/100)))
        elif guild == "Blue Pegasus" and num > 10:
            print("Total %d Jewel" %((num*12800)*(95/100)))
        else:
            print("Total %d Jewel" %(num*12800))
    else:
        num = int(input())
        print("Total %d Jewel" %(num*12800))
main()
