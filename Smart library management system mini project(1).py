# 📚 SMART LIBRARY MANAGEMENT SYSTEM

import datetime
import os
import json
import matplotlib.pyplot as plt
from PIL import Image

library = []

# -------------------- COUNTERS --------------------

add_count = 0
search_count = 0
issue_count = 0
return_count = 0


# -------------------- SHOW LIBRARY IMAGE --------------------

def show_library_image():

    try:
        img = Image.open(r"C:\Users\Srinithi S\Downloads\fe484cdf-45b4-4a85-8046-0bc7ef7f45fe_4032x3024.jpg")   
        img.show()
    except:
        print("❌ Library image not found!")





# -------------------- CLEAR SCREEN --------------------

def clear():

    os.system("cls" if os.name == "nt" else "clear")

# -------------------- SAVE DATA --------------------

def save_data():

    with open("library_data.json", "w") as file:

        json.dump(library, file)

# -------------------- LOAD DATA --------------------

def load_data():

    global library

    try:

        with open("library_data.json", "r") as file:

            library = json.load(file)

    except:

        library = []

# -------------------- DASHBOARD --------------------

def dashboard():

    total = len(library)

    available = 0
    issued = 0

    for book in library:

        if book["status"] == "Available":

            available += 1

        else:

            issued += 1

    print("\n📊 LIBRARY DASHBOARD 📊")

    print(f"📚 Total Books     : {total}")
    print(f"✅ Available Books : {available}")
    print(f"📕 Issued Books    : {issued}")

# -------------------- ADD BOOK --------------------

def add_book():

    global add_count

    book_id = input("Enter Book ID: ")

    # Duplicate ID check
    for book in library:

        if book["id"] == book_id:

            print("\n❌ Book ID already exists!\n")

            return

    book_name = input("Enter Book Name: ")

    category = input("Enter Category: ")

    added_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "id": book_id,
        "name": book_name,
        "category": category,
        "date": added_date,
        "status": "Available"
    }

    library.append(book)

    add_count += 1

    save_data()

    print("\n✅ Book Added Successfully!\n")

# -------------------- VIEW BOOKS --------------------

def view_books():

    if len(library) == 0:

        print("\n❌ No books available.\n")

    else:

        print("\n📚 ------ BOOK LIST ------ 📚")

        for book in library:

            print("="*40)

            print(f"📖 Book ID    : {book['id']}")
            print(f"📘 Book Name  : {book['name']}")
            print(f"📂 Category   : {book['category']}")
            print(f"📅 Added Date : {book['date']}")
            print(f"📌 Status     : {book['status']}")

            print("="*40)

# -------------------- SEARCH BOOK --------------------

def search_book():

    global search_count

    search = input("Enter book name to search: ")

    found = False

    for book in library:

        # Partial Search
        if search.lower() in book["name"].lower():

            print("\n✅ Book Found!")

            print("="*40)

            print(f"📖 Book ID    : {book['id']}")
            print(f"📘 Book Name  : {book['name']}")
            print(f"📂 Category   : {book['category']}")
            print(f"📌 Status     : {book['status']}")

            print("="*40)

            found = True

    search_count += 1

    if found == False:

        print("\n❌ Book not found.\n")

# -------------------- ISSUE BOOK --------------------

def issue_book():

    global issue_count

    book_id = input("Enter Book ID to issue: ")

    for book in library:

        if book["id"] == book_id:

            if book["status"] == "Available":

                student = input("Enter Student Name: ")

                book["status"] = f"Issued to {student}"

                issue_count += 1

                save_data()

                print("\n✅ Book Issued Successfully!\n")

            else:

                print("\n❌ Book already issued.\n")

            return

    print("\n❌ Book ID not found.\n")

# -------------------- RETURN BOOK --------------------

def return_book():

    global return_count

    book_id = input("Enter Book ID to return: ")

    for book in library:

        if book["id"] == book_id:

            if "Issued" in book["status"]:

                late_days = int(input("Enter late days: "))

                fine = late_days * 10

                print(f"\n💰 Fine Amount: ₹{fine}")

                book["status"] = "Available"

                return_count += 1

                save_data()

                print("\n✅ Book Returned Successfully!\n")

            else:

                print("\n❌ This book was not issued.\n")

            return

    print("\n❌ Book ID not found.\n")

# -------------------- DELETE BOOK --------------------

def delete_book():

    book_id = input("Enter Book ID to delete: ")

    for book in library:

        if book["id"] == book_id:

            library.remove(book)

            save_data()

            print("\n🗑️ Book Deleted Successfully!\n")

            return

    print("\n❌ Book not found.\n")

# -------------------- CATEGORY FILTER --------------------

def category_filter():

    category = input("Enter category: ")

    found = False

    for book in library:

        if book["category"].lower() == category.lower():

            print(f"📘 {book['name']}")

            found = True

    if found == False:

        print("\n❌ No books found.\n")

# -------------------- GRAPH --------------------

def show_graph():

    operations = ["Add", "Search", "Issue", "Return"]

    counts = [add_count, search_count, issue_count, return_count]

    plt.bar(operations, counts)

    plt.title("Library Operations")

    plt.xlabel("Operations")

    plt.ylabel("Count")

    plt.show()

# -------------------- LOGIN --------------------

username = input("Enter Username: ")

password = input("Enter Password: ")

if username == "admin" and password == "1234":

    print("\n✅ Login Successful!\n")

else:

    print("\n❌ Invalid Login!\n")

    exit()
if username == "admin" and password == "1234":

    print("\n✅ Login Successful!\n")

    show_library_image()   # Image Display

else:

    print("\n❌ Invalid Login!\n")

    exit()
   

# -------------------- LOAD DATA --------------------

load_data()

# -------------------- MAIN PROGRAM --------------------

while True:

    clear()

    print("="*50)
    print("📚 SMART LIBRARY MANAGEMENT SYSTEM 📚")
    print("="*50)

    dashboard()

    print("""

1️⃣ Add Book
2️⃣ View Books
3️⃣ Search Book
4️⃣ Issue Book
5️⃣ Return Book
6️⃣ Delete Book
7️⃣ Category Filter
8️⃣ Show Graph
9️⃣ Exit

""")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_book()

    elif choice == "2":

        view_books()

    elif choice == "3":

        search_book()

    elif choice == "4":

        issue_book()

    elif choice == "5":

        return_book()

    elif choice == "6":

        delete_book()

    elif choice == "7":

        category_filter()

    elif choice == "8":

        show_graph()

    elif choice == "9":

        print("""
=====================================
🙏 THANK YOU FOR USING
SMART LIBRARY SYSTEM 📚
=====================================
""")

        break

    else:

        print("\n❌ Invalid Choice!\n")

    input("\nPress Enter to continue...")

