"""Prepro"""
def main():
    """koh52"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    nume = int(input())
    cnuma = (numa*3*30)/1000
    cnumb = (numb*30)/1000
    cnumc = (numc*0.5*30)/1000
    cnumd = ((numd*5*30)/1000)*4
    cnume = (nume*24*30)/1000
    print("TV " + str(numa) +" Watt 1 ea " + '''for''' + " 3 hours\n%.2f unit." %cnuma)
    print("Microwave " + str(numb) +" Watt 1 ea " + '''for''' + " 1 hours\n%.2f unit." %cnumb)
    print("Hair dryer " + str(numc) +" Watt 1 ea " + '''for''' + " 0.5 hours\n%.2f unit." %cnumc)
    print("light bulb " + str(numd) +" Watt 4 ea " + '''for''' + " 5 hours\n%.2f unit." %cnumd)
    print("Refrigerator " + str(nume) +" Watt 1 ea " + '''for''' + " 24 hours\n%.2f unit." %cnume)
main()
