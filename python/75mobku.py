"""Prepro"""
def main():
    """75mobku"""
    money = float(input())
    bill = [] 
    round1 = 0
    for _ in range(1, 11):
        round1 = _
        for k in range(1, 6):
            k = k
            cal = float(input())
            bill.append((cal, round1))
            if money >= cal:
                break
        if money >= cal:
            break    
    if money < cal:
        bill.sort(key=lambda x: x[0])
        print("%.2f" %(bill[0][0]))
        print(bill[0][1])
    else:
        print("%.2f" %cal)
        print(round1)
main()
