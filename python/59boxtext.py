"""Prepro"""
def box():
    "box=1"
    return '''-------------------------
|                       |
|                       |
|                       |
|   Pre-Progamming 65   |
|                       |
|                       |
|                       |
-------------------------'''
def boxnon():
    "box>1"
    return '''|                       |
|                       |
|                       |
|   Pre-Progamming 65   |
|                       |
|                       |
|                       |
-------------------------\n'''
def main():
    """59."""
    num1 = int(input())
    if num1 == 1:
        print(box())
    else:
        print(box())
        print("%s" %(boxnon()*(num1-1)))
main()
