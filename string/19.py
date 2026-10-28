#Check whether a given substring exists in the main string. 

main = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in main:
    print("substring exists")
else:
    print("substring does not exist")