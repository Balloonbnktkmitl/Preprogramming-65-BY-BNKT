"""Prepro"""
def main():
    """47."""
    num = int(input())
    bina = (str(bin(num))[2:].replace("0", "close, ")).replace("1", "open, ")
    print(bina[:-2])
main()
