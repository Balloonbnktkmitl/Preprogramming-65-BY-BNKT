"""Quiz"""
def main():
    """Nintendo Battery"""
    batt = int(input())
    leng = int(input())
    print("(%s%s) %d%" %(("O"*(batt//leng)), ("_"*((100-batt)//leng)), batt))
main()
