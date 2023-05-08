"""Quiz"""
def main():
    """Nintendo Battery"""
    batt = int(input())
    leng = int(input())
    mee = ("O"*(int((batt/100)*leng)))
    mod1 = leng - len(mee)
    modb = "_"*(mod1)
    print("("+mee+modb+")"+" "+str(batt)+"%")
main()
