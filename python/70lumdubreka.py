"""Prepro"""
def main():
    """69lumdub"""
    numa1 = float(input())
    numn = int(input())
    numr = float(input())
    numstart = 0
    typ = ""
    if numn == 0 or numr == 0:
        numn = numn
    else:
        while  numstart < numn-1:
            typ = typ + " " + str('{:.2f}'.format(numa1 *(numr**(numstart+1))))
            numstart += 1
        print(str('{:.2f}'.format(numa1))+typ)
main()
