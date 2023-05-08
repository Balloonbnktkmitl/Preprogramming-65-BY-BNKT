"""Prepro"""
def main():
    """44."""
    sex = (input()).upper()
    id1 = input()
    name = input()
    sur = input()
    age = int(input())
    job = input()
    sex1 = sex.replace("FEMALE", "Mrs. ").replace("MALE", "Mr. ")
    print("======")
    print("ID : "+id1[:6])
    print("Name : "+sex1+name.capitalize()+" "+sur.capitalize())
    print("Age : "+str(age)+" years old")
    print("Occupation : "+job.upper())
    print("======")
main()
