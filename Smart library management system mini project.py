import datetime
import os
import matplotlib.pyplot as plt
from PIL import Image

#---------------------login--------------------------
user_name=input("Enter the user_name👧🏻👧🏻:")
password=input("Enter the password-xxx:")
if user_name=="admin" and password=="1234":
    print("Login Successfully!")
else:
    print("User not found")
            

# -------------------- COUNTERS --------------------

add_count =0
search_count = 0
issue_count = 0
return_count = 0


library=[]
#---------------------add_book----------------------
def add_book():
    global add_count
    book_id=input("Enter the book_id:")
    book_name=input("enter the book_name:")
    category=input("Enter the categoryy:")
    
    added_date=datetime.datetime.now().strftime("%d-%m-%Y%H:%M:%S:")
    book={"book_id":book_id,
          "book_name":book_name,
          "category":category,
          "date":added_date}
    
    library.append(book)
    add_count += 1
    print("Book succesfully added!")

#---------------------view_book----------------------
def view_book():
    if len(library)==0:
        print("Book not found")
    else:
        print("""------------Book list!-------------""")
        for book in library:
            print(f"""
            Book_id  :{book['book_id']}
            Book_name:{book['book_name']}
            Category :{book['category']}
            added_date:{book['date']}
            """)
#---------------------search_book----------------------
def search_book():
    global search_count
    search=input("Enter the book_name:")
    for book in library:
        if search == book["book_name"]:
            print("Book available")
            search_count += 1
            return
        print("Book not found")
              
#---------------------issue_book----------------------

def issue_book():
    global issue_count
    id=input("Enter the book_id:")
    for book in library:
        if id==book["book_id"]:
            person=input("Enter the person name:")
            print("Book issued successfully!")
            issue_count += 1
            
        else:
            print("Book not found!")
#---------------------return_book----------------------
def return_book():
    global return_count
    id=input("Enter the book_id:")
    for book in library:
        if id==book["book_id"]:
            print("Book return successfully")
            return_count += 1
            
        else:
            print("Book not returned")
#---------------------show_graph----------------------

def show_graph():

    operations = ["Add", "Search", "Issue", "Return"]

    counts = [add_count, search_count, issue_count, return_count]

    plt.bar(operations, counts)

    plt.title("Library Operations")

    plt.xlabel("Operations")

    plt.ylabel("Count")

    plt.show()

#---------------------image show---------------------
def img_show():
    img = Image.open(r"C:\Users\Srinithi S\Downloads\library img.jpg")
    resize_img = img.resize((300, 300))
    resize_img.show()



    

while True:
    print("""
========================================
📒📒SMART LIBRARY MANAGEMENT SYSTEM📒📒
========================================
1.Add_book:
2.View_book:
3.Search_book:
4.Issue_book:
5.Return_book:
6.Show_graph:
7.image_show:
8.Exit
=======================================
THANK YOU!!!🤝🙏🏻🙏🏻
=======================================
""")

    ch=input("Enter choice:")
    if ch=="1":
       add_book()
    elif ch=="2":
       view_book()
    elif ch=="3":
       search_book()
    elif ch=="4":
        issue_book()
    elif ch=="5":
        return_book()
    elif ch=="6":
        show_graph()
    elif ch=="7":
        img_show()
    elif ch=="8":
        print("THANK YOU")
        break
    else:
       print("invalid")





   
    

    
                     
            
    



    
