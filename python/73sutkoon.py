"""Prepro"""
def main():
    """73sutkoon"""
    num = int(input())
    koon = int(input())
    if num >= 2 and koon > 0:
        for i in range(2, num+1):
            print("-----")
            for j in range(1, koon+1):
                print("%d x %d = %d" %(i, j, i*j))
                j += 1
            i += 1
    print("-----")
main()
