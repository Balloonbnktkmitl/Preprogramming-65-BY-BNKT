"""Prepro"""
def main():
    """69lumdub"""
    numa1 = int(input())
    numn = int(input())
    numd = int(input())
    numstart = 0
    typ = ""
    if numn == 0:
        numn = numn
    else:
        while  numstart < numn-1:
            typ = typ + " " + str(numa1 +((numstart+1)*numd))
            numstart += 1
        print(str(numa1)+typ)
main()
