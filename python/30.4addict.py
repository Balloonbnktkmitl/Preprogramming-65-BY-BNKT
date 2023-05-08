"""Prepro"""
def main():
    """30."""
    number = float(input())
    word = input()
    cal = ((((number+4)**(1/4))+(number/4))/((4*number)-4))*44
    cal2 = int(number/44)
    print(word*cal2)
    print("%.4f" %cal)
main()
