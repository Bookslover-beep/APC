#21. Maintain book records containing book ID, title, author, and availability status. 
#Implement operations to:  
#•Add a book.  
#•Search for a book.  
#•Issue a book.  
#•Return a book.  
#•Display available books. 


FILENAME = "books.txt"

def add_book():
    b_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    with open(FILENAME, "a") as f:
        f.write(f"{b_id}|{title}|{author}|Available\n")
    print("Book added successfully!")

def search_book():
    key = input("Enter Book ID or Title to search: ").lower()
    with open(FILENAME, "r") as f:
        for line in f:
            if key in line.lower():
                print(line.strip().replace("|", " | "))

def update_status(new_status):
    b_id = input("Enter Book ID: ")
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    with open(FILENAME, "w") as f:
        for line in lines:
            parts = line.strip().split("|")
            if parts[0] == b_id:
                parts[3] = new_status
            f.write("|".join(parts) + "\n")
    print("Status updated successfully!")

def display_available():
    print("\n--- Available Books ---")
    with open(FILENAME, "r") as f:
        for line in f:
            if "Available" in line:
                print(line.strip().replace("|", " | "))

while True:
    print("\n1. Add | 2. Search | 3. Issue | 4. Return | 5. Display Available | 6. Exit")
    choice = input("Enter choice (1-6): ")
    
    if choice == '1': add_book()
    elif choice == '2': search_book()
    elif choice == '3': update_status("Issued")
    elif choice == '4': update_status("Available")
    elif choice == '5': display_available()
    elif choice == '6': break