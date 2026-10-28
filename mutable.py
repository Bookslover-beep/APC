#Mutable or Immutable

# 1. List(mutable)

print("----------List------------"
list1 = [1, 2, "Python", "Programming", 15.9]

print("list1 = ", list1)
print("type:", type(list1))
print("before id:", id(list1))

list1.append("Hello")
print("After appending:")
print("list1 = ", list1)
print("ID after:", id(list1))

if id(list1) == id(list1):
    print("List is mutable")

# 2. Tuple(Immutable)
print("\n-----------Tuple-----------")
tuple1 = (1, 2, "Python", "Programming", 15.9)
print("tuple1 = ", tuple1)
print("Type:", type(tuple1))
old_id = id(tuple1)
print("ID before:", old_id)

tuple1 = tuple1 + ("Hello",)
print("tuple1 = ", tuple1)
print("ID after:", id(tuple1))

if old_id != id(tuple1):
    print("Tuple is Immutable")

# 3. String(Immutable)
print("\n-----------STRING----------- ")

string1 = "Python"
print("string1 = ", string1)
print("Type:", type(string1))
old_id = id(string1)
print("ID before:", old_id)

string1 = string1 + " Programming"
print("string1 = ", string1)
print("ID after:", id(string1))

if old_id != id(string1):
    print("String is Immutable")

# 4. Set(Mutable)
print("\n-----------Set----------- ")

set1 = {10, 20, 30, 40}
print("set1 = ", set1)
print("Type:", type(set1))
old_id = id(set1)
print("ID before:", old_id)

set1.add(50)
print("set1 = ", set1)
print("ID after:", id(set1))

if old_id == id(set1):
    print("Set is Mutable")

# 5. Dictionary(Mutable)
print("\n----------- Dictionary-----------")
dict1 = {
    "Name": "Ryan",
    "Age": 20,
    "Course": "Python"
}
print("dict1 = ", dict1)
print("Type:", type(dict1))
old_id = id(dict1)
print("ID before:", old_id)

dict1["Age"] = 21
dict1["City"] = "Mumbai"
print("dict1 = ", dict1)
print("ID after:", id(dict1))

if old_id == id(dict1):
    print("Dictionary is Mutable")