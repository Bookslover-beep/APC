#A company insures its drivers in the following cases:
#- If the driver is married.
#- If the driver is unmarried, male and above 30 years of age.
#- If the driver is unmarried, female and above 25 years of age.
         
#In all the other cases, the driver is not insured.
#Write a PYTHON program to determine whether the driver is insured or not

marry = input("Is Driver Married? (yes/no): ")

if marry == "yes":
    print("The driver is insured.")
elif marry == "no":
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))
   
    if gender == "male" and age > 30:
        print("The driver is insured.")
    elif gender == "female" and age > 25:
        print("The driver is insured.")
    else:
        print("The driver is not insured.")
else:
    print("The driver is not insured.")
 