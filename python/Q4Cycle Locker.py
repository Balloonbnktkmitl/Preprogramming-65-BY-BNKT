"""Quiz"""
def cal(las1, las2, las3, las4, tmp):
    """Calculate"""
    if 
        
    while las1 != 0:
        if las1 < 0:
            tmp += 1
            las1 += 1
        else:
            tmp += 1
            las1 -= 1
    while las2 != 0:
        if las2 < 0:
            tmp += 1
            las2 += 1
        else:
            tmp += 1
            las2 -= 1
    while las3 != 0:
        if las3 < 0:
            tmp += 1
            las3 += 1
        else:
            tmp += 1
            las3 -= 1
    while las4 != 0:
        if las4 < 0:
            tmp += 1
            las4 += 1
        else:
            tmp += 1
            las4 -= 1
    print(tmp)
def main():
    """Q4Cycle Locker"""
    pas = input()
    num = input()
    tmp = 0
    las1 = int(pas[0])-int(num[0])
    las2 = int(pas[1])-int(num[1])
    las3 = int(pas[2])-int(num[2])
    las4 = int(pas[3])-int(num[3])
    las5 = int(num[0])-int(num[0])
    las6 = int(num[1])-int(num[1])
    las7 = int(num[2])-int(num[2])
    las8 = int(num[3])-int(num[3])
    if pas == num:
        print(tmp)
    else:
        cal(las1, las2, las3, las4, tmp)

main()
