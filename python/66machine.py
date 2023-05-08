"""Prepro"""
def main():
    """66machine"""
    numstart = int(input())
    numstop = int(input())
    suminte = 0
    inte = ''''''
    if numstart < numstop:
        for i in range(numstart, numstop+1):
            if i % 2 == 1:
                suminte = suminte + i
                inte = str(inte) +" "+ str(i)
        print("Integer Pass :"+str(inte))
        print("Sum Answer : "+str(suminte))
    else:
        while numstart > numstop:
            if numstart % 2 == 1:
                suminte = suminte + numstart
                inte = str(inte) +" "+ str(numstart)
            numstart -= 1
        print("Integer Pass :"+str(inte))
        print("Sum Answer : "+str(suminte))
main()
