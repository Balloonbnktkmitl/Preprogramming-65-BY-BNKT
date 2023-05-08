"""Prepro"""
def main():
    """39."""
    fastsa = int(input())
    timea = input()
    fastsb = int(input())
    timeb = input()
    if timea == "Millisecond":
        fastsa = fastsa*0.001
    elif timea == "Microsecond":
        fastsa = fastsa*(1.0*(10**(-6)))
    elif timea == "Nanosecond":
        fastsa = fastsa*(1.0*(10**(-9)))
    elif  timea == "Picosecond":
        fastsa = fastsa*(1.0*(10**(-12)))
    if timeb == "Millisecond":
        fastsb = fastsb*0.001
    elif timeb == "Microsecond":
        fastsb = fastsb*(1.0*(10**(-6)))
    elif timeb == "Nanosecond":
        fastsb = fastsb*(1.0*(10**(-9)))
    elif  timeb == "Picosecond":
        fastsb = fastsb*(1.0*(10**(-12)))
    if fastsa < fastsb:
        print("Server A, %.6f second\nFaster than server B , %d times" %(fastsa, fastsb//fastsa))
    elif fastsa == fastsb:
        print("equal")
    else:
        print("Server B, %.6f second\nFaster than server A \
, %d times" %(fastsb, float(fastsa)//fastsb))
main()
