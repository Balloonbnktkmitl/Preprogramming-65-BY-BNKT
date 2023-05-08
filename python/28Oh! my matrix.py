"""Prepro"""
def main():
    """28."""
    numa1 = int(input())
    numa2 = int(input())
    numa3 = int(input())
    numa4 = int(input())
    numc1 = int(input())
    numc2 = int(input())
    numc3 = int(input())
    numc4 = int(input())
    numb1 = numc1-numa1
    numb2 = numc2-numa2
    numb3 = numc3-numa3
    numb4 = numc4-numa4
    deta = (numa1*numa4)-(numa2*numa3)
    detb = (numb1*numb4)-(numb2*numb3)
    detc = (numc1*numc4)-(numc2*numc3)
    print("b1: %d\nb2: %d\nb3: %d\nb4: %d\nD: %.2f"\
        %(numb1, numb2, numb3, numb4, float(deta+detb+detc)))
main()
