"""Prepro"""
def main():
    """93mathyak"""
    listnum = input().strip("[",).strip("]").split(",")
    callist =[]
    for i in range(len(listnum)):
        if i == 0:
            callist.append(int(listnum[i]))
        else:
            cal = callist[i-1]+(1//int(listnum[i]))
            callist.append(cal)
    print(callist)
main()

