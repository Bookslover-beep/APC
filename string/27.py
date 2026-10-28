#Validate whether a given email address follows a valid format. 

email = input("Enter Email: ")
if "@" in email and "." in email and email.count("@") == 1:
    print("valid email")
else:
    print("invalid email")
