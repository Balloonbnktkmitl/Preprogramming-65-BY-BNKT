"""Prepro"""
def pat1(val):
    """pat1"""
    for time in range(1, val+1):
        if time % 3 == 0:
            print("..◊.", end="")
        else:
            print("..♦.", end="")
    print(".\n", end="")
def pat2(val):
    """pat2"""
    for time in range(1, val+1):
        if time % 3 == 0:
            print(".◊.◊", end="")
        else:
            print(".♦.♦", end="")
    print(".\n", end="")
def pat3(tex):
    """pat3"""
    time = 0
    print("♦", end="")
    for i in tex:
        time += 1
        print(".%s." %(i), end="")
        if time % 3 == 1:
            print("♦", end="")
        else:
            print("◊", end="")
    print()
def main():
    """87PeterPanframe"""
    word = input()
    valword = len(word)
    pat1(valword)
    pat2(valword)
    pat3(word)
    pat2(valword)
    pat1(valword)
main()
