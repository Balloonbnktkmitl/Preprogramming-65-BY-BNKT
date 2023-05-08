"""Prepro"""
def main():
    """27."""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_x = int(input())
    num_y = int(input())
    cal = (((num_b/((num_a**2)/num_d))+(num_x*(num_b/num_a)))*num_y)/(num_y*num_c)
    print("%.2f" %cal)
main()
