"""Prepro"""
def main():
    """29."""
    sec = int(input())
    day = sec/86400
    sec2 = sec%86400
    hours = sec2/3600
    sec3 = sec2%3600
    minute = sec3/60
    second = sec3%60
    print("%02d:%02d:%02d:%02d" %(day, hours, minute, second))
main()
