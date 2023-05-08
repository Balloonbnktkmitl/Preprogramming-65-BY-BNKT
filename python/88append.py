"""Prepro"""
def main():
    """88append"""
    num = int(input())
    numlist = []
    for i in range(0, num):
        i = i
        numlist.append(input())
    out = "["
    for i in range(0, num):
        out += "\"" + numlist[i] + "\""
        if i != num-1:
            out += ", "
    out += "]"
    print(out)
main()
