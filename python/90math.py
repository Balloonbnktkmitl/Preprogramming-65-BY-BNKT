"""Prepro"""
def main():
    """90math"""
    numall = int(input())
    numlist = []
    for i in range(numall):
        numlist.append(float(input()))
    koon = float(input())
    sumlist = []
    for i in range(numall):
        sumlist.append(str('{:.2f}'.format(numlist[i]*koon)))
    print(sumlist)
main()
