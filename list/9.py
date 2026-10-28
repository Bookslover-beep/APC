#9.Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
cities = ["Mumbai", "Pune", "Delhi", "Kolhapur", "Hyderabad"]
print("cities =",cities)
n = input("Enter a city name: ")

if n in cities:
    print("Exists in cities!")
else:
    print("Does not exist...")