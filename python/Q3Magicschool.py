"""Quiz3"""
def main():
    """Magicschool"""
    name = input()
    age = int(input())
    sex = input().capitalize()
    height = float(input())
    if 13 <= age <= 15:
        if sex == "Male":
            print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
            if height >= 160:
                print("You can study in junior high school.")
            else:
                print("You can not join this school.")
        elif sex == "Female":
            print("Miss %s Age: %d Height: %.2f" %(name, age, height))
            if height >= 155:
                print("You can study in junior high school.")
            else:
                print("You can not join this school.")
    elif 16 <= age <= 18:
        if sex == "Male":
            print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
            if height >= 170:
                print("You can study in senior high school.")
            else:
                print("You can not join this school.")
        elif sex == "Female":
            print("Miss %s Age: %d Height: %.2f" %(name, age, height))
            if height >= 165:
                print("You can study in senior high school.")
            else:
                print("You can not join this school.")
    else:
        if sex == "Male":
            print("Mr. %s Age: %d Height: %.2f" %(name, age, height))
        elif sex == "Female":
            print("Miss %s Age: %d Height: %.2f" %(name, age, height))
        print("You can not join this school.")
main()
