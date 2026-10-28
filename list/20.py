#20.Create a list of books. Implement:
#a.Add a new book b.Search a book c.Remove a book d.Display all books e.Count total books

books = []
print("books =",books)
print()

books.append("Python Basics")
books.append("Data Structures")
books.append("Web Development")
print("After append:\nbooks =",books)
print()

search_book = "Data Structures"
if search_book in books:
    print(f"'{search_book}' found.")
else:
    print(f"'{search_book}' not found.")

books.remove("Web Development")
print("After remove:\nbooks =",books)
print()

print("All books:", books)
print("Total books:", len(books))
