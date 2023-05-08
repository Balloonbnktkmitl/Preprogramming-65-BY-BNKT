"""Prepro"""
def thailand():
    """Prepro"""
    free = 0
    age = int(input())
    if age > 10 and age <= 20:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(20)))
        else:
            num = int(input())
            print("%.2f" %(float(20*((100-num)/100))))
    elif age > 20 and age <= 60:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(40)))
        else:
            num = int(input())
            print("%.2f" %(float(40*((100-num)/100))))
    else:
        print("%.2f" %free)
def tangdao():
    """Prepro"""
    free = 0
    age = int(input())
    if age > 10 and age <= 20:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(20*5)*0.5))
        else:
            num = int(input())
            print("%.2f" %(float(((20*5)*((100-num)/100)*0.5))))
    elif age > 20 and age <= 60:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(40*5)*0.5))
        else:
            num = int(input())
            print("%.2f" %(float(((40*5)*((100-num)/100))*0.5)))
    else:
        print("%.2f" %free)
def tangdao1():
    """Prepro"""
    free = 0
    age = int(input())
    if age > 10 and age <= 20:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(20*5)))
        else:
            num = int(input())
            print("%.2f" %(float((20*5)*((100-num)/100))))
    elif age > 20 and age <= 60:
        coupon = input()
        if coupon == "N":
            print("%.2f" %(float(40*5)))
        else:
            num = int(input())
            print("%.2f" %(float((40*5)*((100-num)/100))))
    else:
        print("%.2f" %free)
def main():
    """41."""
    thai = input()
    if thai == "N":
        nation = input()
        if nation != "Vietnam" and nation != "Singapore" and nation != "India":
            tangdao1()
        else:
            tangdao()
    else:
        thailand()
main()
