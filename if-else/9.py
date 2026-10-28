#Write a PYTHON program to check a year for leap year.
 
year = int(input("Enter the year:"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"The {year} is leap year.")
else:
    print(f"The {year} is not leap year.")