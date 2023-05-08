"""Prepro"""
def main():
    """81kuaundub"""
    num = int(input())
    for row in range(1, (2*num)+2):
        for column in range(1, (2*num)+2):
            print("(%02d, %02d)" %(abs(row-num-1), abs(column-num- 1)), end=' ')
        print()
main()
