"""Prepro"""
def layerinput(deep):
    "Deep layer"
    if 0 <= deep <= 1350:
        layer = "1st Layer : Edge of the Abyss"
    elif deep <= 2600:
        layer = "2nd Layer : Forest of Temptation"
    elif deep <= 7000:
        layer = "3rd Layer : Great Fault"
    elif deep <= 12000:
        layer = "4th Layer : The Goblets of Giants"
    elif deep <= 13000:
        layer = "5th Layer : Sea of Corpses"
    elif deep <= 15500:
        layer = "6th Layer : The Capital of the Unreturned"
    else:
        layer = "7th Layer : The Final Maelstrom"
    return layer
def curseinput(tmp, deep):
    "curse"
    if tmp == "UP":
        if 0 <= deep <= 1350:
            curse = "Curse : Light dizziness and nausea."
        elif deep <= 2600:
            curse = "Curse : Intense nausea, headaches, and numbness of limbs."
        elif deep <= 7000:
            curse = "Curse : Vertigo combined with visual and auditory hallucinations."
        elif deep <= 12000:
            curse = "Curse : Intense pain throughout the body and bleeding from every orifice."
        elif deep <= 13000:
            curse = "Curse : Complete sensory deprivation, confusion and self-harming behavior."
        elif deep <= 15500:
            curse = "Curse : Loss of humanity or death, or under specific conditions, the Blessing."
        else:
            curse = "Curse : Certain death."
    else:
        curse = "Curse : -"
    return curse
def main():
    """56Deep In Abyss"""
    pla1 = input()
    deep1 = int(input())
    tmp1 = input().upper()
    pla2 = input()
    deep2 = int(input())
    tmp2 = input().upper()
    pla3 = input()
    deep3 = int(input())
    tmp3 = input().upper()
    print("Name : %s\n%s\n%s\n---" %(pla1, layerinput(deep1), curseinput(tmp1, deep1)))
    print("Name : %s\n%s\n%s\n---" %(pla2, layerinput(deep2), curseinput(tmp2, deep2)))
    print("Name : %s\n%s\n%s" %(pla3, layerinput(deep3), curseinput(tmp3, deep3)))
main()
