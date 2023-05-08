"""Prepro"""
def main():
    """74kuaundub"""
    numi = int(input())
    numj = int(input())
    if numi >= 1 and numj >= 1:
        for i in range(1, numi+1):
            for j in range(1, numj+1):
                print("(%d, %d)" %(i, j), end=" ")
                if j == numj:
                    print("")
                j += 1
main()
