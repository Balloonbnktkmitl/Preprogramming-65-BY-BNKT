"""Prepro"""
def main():
    """54Composite Function"""
    num = float(input())
    typ = input().lower()
    funf = (15+num-(num**3))/(((num**2)/3)+11)
    fung = (num**3)+(4*(num))-1
    if typ == "fog":
        cal = (15+fung-(fung**3))/(((fung**2)/3)+11)
        print("%.2f" %cal)
    else:
        cal = (funf**3)+(4*funf)-1
        print("%.2f" %cal)
main()
