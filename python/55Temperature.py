"""Prepro"""
def cel(temp, temper):
    "Celsius"
    if temper == "C→F":
        print("Fahrenheit = %.2f" %((temp*(9/5))+32))
    elif temper == "C→K":
        print("Kelvin = %.2f" %(temp+273.15))
    elif temper == "C→R":
        print("Rankine = %.2f" %((temp+273.15)*(9/5)))
    elif temper == "C→C":
        print("Celsius = %.2f" %temp)
def fah(temp, temper):
    "Fahrenheit"
    if temper == "F→C":
        print("Celsius = %.2f" %((temp-32)*(5/9)))
    elif temper == "F→K":
        print("Kelvin = %.2f" %((temp+459.67)*(5/9)))
    elif temper == "F→R":
        print("Rankine = %.2f" %(temp+459.67))
    elif temper == "F→F":
        print("Fahrenheit = %.2f" %temp)
def kel(temp, temper):
    "Kelvin"
    if temper == "K→C":
        print("Celsius = %.2f" %(temp-273.15))
    elif temper == "K→F":
        print("Fahrenheit = %.2f" %((temp*(9/5))-459.67))
    elif temper == "K→R":
        print("Rankine = %.2f" %(temp*(9/5)))
    elif temper == "K→K":
        print("Kelvin = %.2f" %temp)
def rank(temp, temper):
    "Rankine"
    if temper == "R→C":
        print("Celsius = %.2f" %((temp-491.67)*5/9))
    elif temper == "R→F":
        print("Fahrenheit = %.2f" %(temp-459.67))
    elif temper == "R→K":
        print("Kelvin = %.2f" %(temp*5/9))
    elif temper == "R→R":
        print("Rankine = %.2f" %temp)
def main():
    """55Temperature"""
    temp = float(input())
    temper = input().upper()
    if temper[0] == "C":
        cel(temp, temper)
    elif temper[0] == "F":
        fah(temp, temper)
    elif temper[0] == "K":
        kel(temp, temper)
    elif temper[0] == "R":
        rank(temp, temper)
main()
