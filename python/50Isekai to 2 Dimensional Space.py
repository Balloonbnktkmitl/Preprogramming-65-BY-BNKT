"""Prepro"""
import math

def main():
    """50."""
    pointx = float(input())
    pointy = float(input())
    kajud = float(input())
    deg = float(input())
    radx = abs(math.radians(deg))
    rady = abs(math.radians(deg))
    disx = math.cos(radx)*kajud
    disy = math.sin(rady)*kajud
    totalx = pointx + disx
    totaly = pointy + disy
    print("%.2f" %totalx)
    print("%.2f" %totaly)
main()
