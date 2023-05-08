"""Prepro"""
def main():
    """35."""
    tun = input()
    tun2 = input()
    if (tun == "Calm" and tun2 == "Empathetic") or (tun2 == "Calm" and tun == "Empathetic"):
        print("Ice")
    elif (tun == "Reliable" and tun2 == "Courageous") or \
        (tun2 == "Reliable" and tun == "Courageous"):
        print("Fern")
    elif (tun == "Optimistic" and tun2 == "Cheerful") or \
        (tun2 == "Optimistic" and tun == "Cheerful"):
        print("Bam")
    elif (tun == "Attractive" and tun2 == "Creative") or \
        (tun2 == "Attractive" and tun == "Creative"):
        print("Tangmo")
    elif (tun == "Creative" and tun2 == "Cheerful") or \
        (tun2 == "Creative" and tun == "Cheerful"):
        print("Mild")
    elif (tun == "Reliable" and tun2 == "Optimistic") or \
        (tun2 == "Reliable" and tun == "Optimistic"):
        print("Prae")
    elif (tun == "Courageous" and tun2 == "Calm") or \
        (tun2 == "Courageous" and tun == "Calm"):
        print("Dream")
    elif (tun == "Empathetic" and tun2 == "Attractive") or \
        (tun2 == "Empathetic" and tun == "Attractive"):
        print("Aom")
main()
