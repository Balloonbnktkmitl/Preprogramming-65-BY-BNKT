"""Prepro"""
def main():
    """92Mala xiang guo"""
    veg = ["celery stalks", "carrots", "potatoes", "mushrooms", "tofu", "lotus root", "cabbage", \
"instant noodles", "glass noodle", "wonton", \
"beef", "pork loin", "chicken", "fish balls", "cheese ball", \
"octopus", "fish", "shrimp", "mussels", \
"Mild", "Medium", "Hot", "Extra hot", "stop"]
    taste = ["Mild", "Medium", "Hot", "Extra hot"]
    billlist = []
    tmp = ""
    while tmp != "stop":
        tmp = (input().lower()).replace("1", "Mild").replace("2", "Medium").replace("3", "Hot")\
.replace("4", "Extra hot")
        if tmp not in veg:
            billlist.append("getout")
        else:
            billlist.append(tmp)
    if billlist[0] == "stop" or (len(billlist) == 2 and billlist[0] in taste):
        print("Huh? you didn't order anything!")
    elif "getout" in billlist:
        print("Get out!")
    elif billlist[-2] in taste:
        print("%s Mala xiang guo is here." %(billlist[-2]))
    elif billlist[-2] not  in taste:
        print("Please choose a spicy level!")
    else:
        print("Get out!")
main()
