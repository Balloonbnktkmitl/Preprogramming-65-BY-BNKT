"""Prepro"""
def fibonacci(num):
    """60.Fibonacci"""
    if num < 0:
        pass
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
def main():
    "fibonacci"
    numx = int(input())
    print(fibonacci(numx))
main()
