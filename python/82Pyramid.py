"""Prepro"""
def main():
    """82Pyramid"""
    num = int(input())
    col = 0
    for row in range(1, num+1):
        for j in range(1, (num-row)+1):
            j = j
            print(end='  ')
        while col != 2*row-1:
            print("* ", end='')
            col += 1
        col = 0
        print()
main()
