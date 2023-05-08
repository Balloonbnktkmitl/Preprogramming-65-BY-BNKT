"""Prepro"""
def main():
    """79Simple matrix"""
    row = int(input())
    num = int(input())
    for i in range(1, row+1):
        for j in range(1, num+1):
            print(j*i, end=' ')
        print()
main()
