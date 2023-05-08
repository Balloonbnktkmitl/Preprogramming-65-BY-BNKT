"""Prepro"""
def main():
    """40."""
    moneycus = float(input())
    bill = float(input())
    mon = moneycus-bill
    if moneycus < bill:
        print("จำนวนเงินไม่พอ")
    elif moneycus == bill:
        print("จ่ายมาพอดี")
    else:
        bank100 = mon//100
        cal = mon%100
        bank50 = cal//50
        cal = cal%50
        bank20 = cal//20
        cal = cal%20
        bank12 = cal//12
        cal = cal%12
        bank10 = cal//10
        cal = cal%10
        bank5 = cal//5
        cal = cal%5
        bank2 = cal//2
        bank1 = cal%2
        cal = mon%1
        bank050 = cal//0.5
        cal = cal%0.5
        bank025 = cal//0.25
        print("เเบงค์ 100 บาท : %d" %bank100)
        print("เเบงค์ 50 บาท : %d" %bank50)
        print("เเบงค์ 20 บาท : %d" %bank20)
        print("เหรียญ 12 บาท : %d" %bank12)
        print("เหรียญ 10 บาท : %d" %bank10)
        print("เหรียญ 5 บาท : %d" %bank5)
        print("เหรียญ 2 บาท : %d" %bank2)
        print("เหรียญ 1 บาท : %d" %bank1)
        print("เหรียญ 50 สตางค์ : %d" %bank050)
        print("เหรียญ 25 สตางค์ : %d" %bank025)
main()
