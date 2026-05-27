# Hostel Management System
# Existing Features + Smart Room Recommendation Module

# ------------------------------
# Hostel Data Storage
# ------------------------------

students = []

rooms = {
    101: {"type": "AC", "capacity": 2, "students": []},
    102: {"type": "Non-AC", "capacity": 2, "students": []},
    103: {"type": "AC", "capacity": 2, "students": []},
    104: {"type": "Non-AC", "capacity": 2, "students": []}
}

fees = {}

complaints = []


# ------------------------------
# 1. Add Student
# ------------------------------

def add_student():

    student_id = input("Enter Student ID : ")
    name = input("Enter Name : ")
    department = input("Enter Department : ")

    student = {
        "id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)

    print("Student Added Successfully")


# ------------------------------
# 2. View Students
# ------------------------------

def view_students():

    if len(students) == 0:
        print("No Student Records Found")

    else:
        for student in students:
            print(student)


# ------------------------------
# 3. Search Student
# ------------------------------

def search_student():

    search_name = input("Enter Student Name : ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("Student Found")
            print(student)

            found = True

    if found == False:
        print("Student Not Found")


# ------------------------------
# 4. Fee Management
# ------------------------------

def pay_fee():

    student_id = input("Enter Student ID : ")
    amount = input("Enter Fee Amount : ")

    fees[student_id] = amount

    print("Fee Paid Successfully")


# ------------------------------
# 5. Complaint Management
# ------------------------------

def add_complaint():

    complaint = input("Enter Complaint : ")

    complaints.append(complaint)

    print("Complaint Added Successfully")


# ------------------------------
# 6. View Complaints
# ------------------------------

def view_complaints():

    if len(complaints) == 0:
        print("No Complaints")

    else:
        for complaint in complaints:
            print(complaint)


# ------------------------------
# 7. Smart Room Recommendation
# ------------------------------

def recommend_room():

    department = input("Enter Department : ")
    preference = input("Enter Room Preference (AC / Non-AC) : ")

    found = False

    print("\nRecommended Rooms:\n")

    for room_no, details in rooms.items():

        # Check room preference
        if details["type"].lower() == preference.lower():

            # Check room capacity
            if len(details["students"]) < details["capacity"]:

                # Same department or empty room
                if department in details["students"] or len(details["students"]) == 0:

                    print("Room Number :", room_no)
                    print("Room Type   :", details["type"])
                    print("Students    :", details["students"])
                    print("----------------------")

                    found = True

    if found == False:
        print("No Suitable Room Found")


# ------------------------------
# 8. Allocate Room
# ------------------------------

def allocate_room():

    name = input("Enter Student Name : ")
    department = input("Enter Department : ")
    room_no = int(input("Enter Room Number : "))

    if room_no in rooms:

        if len(rooms[room_no]["students"]) < rooms[room_no]["capacity"]:

            rooms[room_no]["students"].append(department)

            print("Room Allocated Successfully")

        else:
            print("Room Full")

    else:
        print("Invalid Room Number")


# ------------------------------
# 9. View Rooms
# ------------------------------

def view_rooms():

    for room_no, details in rooms.items():

        print("Room Number :", room_no)
        print("Room Type   :", details["type"])
        print("Capacity    :", details["capacity"])
        print("Students    :", details["students"])
        print("----------------------")


# ------------------------------
# Main Menu
# ------------------------------

while True:

    print("\n===== HOSTEL MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Pay Fee")
    print("5. Add Complaint")
    print("6. View Complaints")
    print("7. Recommend Room")
    print("8. Allocate Room")
    print("9. View Rooms")
    print("10. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        pay_fee()

    elif choice == "5":
        add_complaint()

    elif choice == "6":
        view_complaints()

    elif choice == "7":
        recommend_room()

    elif choice == "8":
        allocate_room()

    elif choice == "9":
        view_rooms()

    elif choice == "10":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
