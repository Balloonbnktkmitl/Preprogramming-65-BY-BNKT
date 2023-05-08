"""tammaidaika"""
def main():
    """tammaidaika"""
    name = input()
    age = int(input())
    sex = input()
    height = float(input())
    if age>=13 and age<=15:
        if sex == ("Male") :
            if height >= 160:
                print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
                print("You can study in junior high school.")
            else:
                print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
                print("You can not join this school.")
        elif sex == ("Female") :
            if height >= 155 :
                print("Miss %s Age: %d Height: %.2f" %(name, age, height))
                print("You can study in junior high school.")
            else:
                print("Miss %s Age: %d Height: %.2f" %(name, age, height))
                print("You can not join this school.")
    elif age>=16 and age<=18:
        if sex == ("Male") :
            if height >= 170 :
                print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
                print("You can study in senior high school.")
            else :
                print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
                print("You can not join this school.")
        elif sex == ("Female") :
            if height>=165 :
                print("Miss %s Age: %d Height: %.2f" %(name, age, height))
                print("You can study in senior high school.")
            else :
                print("Miss %s Age: %d Height: %.2f" %(name, age, height))
                print("You can not join this school.")
    else:
        if sex == "Male" :
            print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
            print("You can not join this school.")
        elif sex == "Female" :
            print("Miss %s Age: %d Height: %.2f" %(name, age, height))
            print("You can not join this school.")
main()
