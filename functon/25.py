#25.Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

library = {}

def add_book(book_id, title):
    library[book_id] = {"title": title, "status": "Available"}

def issue_book(book_id):
    if book_id in library and library[book_id]["status"] == "Available":
        library[book_id]["status"] = "Issued"
        return True
    return False

def return_book(book_id):
    if book_id in library:
        library[book_id]["status"] = "Available"

def search_book(title):
    return [b_id for b_id, details in library.items() if details["title"].lower() == title.lower()]

def display_available():
    return {b_id: details for b_id, details in library.items() if details["status"] == "Available"}

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Available Books")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")
    
    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        add_book(book_id, title)
        print("Book added successfully.")
    elif choice == '2':
        book_id = input("Enter Book ID to issue: ")
        if issue_book(book_id):
            print("Book issued successfully.")
        else:
            print("Book is either already issued or invalid ID.")
    elif choice == '3':
        book_id = input("Enter Book ID to return: ")
        if book_id in library:
            return_book(book_id)
            print("Book returned successfully.")
        else:
            print("Invalid Book ID.")
    elif choice == '4':
        title = input("Enter title to search: ")
        results = search_book(title)
        print(f"Found Book IDs: {results if results else 'No matching books found'}")
    elif choice == '5':
        avail = display_available()
        print("--- Available Books ---")
        if avail:
            for b_id, details in avail.items():
                print(f"ID: {b_id} | Title: {details['title']}")
        else:
            print("No books currently available.")
    elif choice == '6':
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")