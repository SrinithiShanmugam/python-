from tkinter import *
from tkinter import messagebox
import json
import os
import subprocess
import sys

USER_FILE = "users.json"


# ── Helper functions ─────────────────────────────────────────────────────────
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)


# ── Login Window ──────────────────────────────────────────────────────────────
root = Tk()
root.title("AI Assistant - Login")
root.geometry("400x400")
root.config(bg="SKY BLUE")
root.resizable(False, False)

Label(root, text="AI ASSISTANT", font=("Comic Sans MS", 18, "bold"), bg="SKY BLUE").pack(pady=20)

Label(root, text="Username", font=("Arial", 12), bg="SKY BLUE").pack(pady=(10, 0))
username_entry = Entry(root, font=("Arial", 12), justify=CENTER)
username_entry.pack(pady=5, ipady=4)

Label(root, text="Password", font=("Arial", 12), bg="SKY BLUE").pack(pady=(10, 0))
password_entry = Entry(root, font=("Arial", 12), justify=CENTER, show="*")
password_entry.pack(pady=5, ipady=4)

status_label = Label(root, text="", font=("Arial", 10), fg="red", bg="SKY BLUE")
status_label.pack(pady=5)


# ── Button Functions ──────────────────────────────────────────────────────────
def signup():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        status_label.config(text="Please fill all fields")
        return

    users = load_users()

    if username in users:
        status_label.config(text="Username already exists!")
        return

    users[username] = password
    save_users(users)

    status_label.config(text="", fg="red")
    messagebox.showinfo("Success", "Account created! Please login now.")
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        status_label.config(text="Please fill all fields")
        return

    users = load_users()

    if username not in users:
        status_label.config(text="User not found. Please signup first.")
        return

    if users[username] != password:
        status_label.config(text="Incorrect password!")
        return

    # ✅ Login success → open AI Assistant
    root.destroy()
    subprocess.Popen([sys.executable, "test.py"])


# ── Buttons ───────────────────────────────────────────────────────────────────
Button(root, text="LOGIN", bg="#356696", fg="white", font=("Arial", 11, "bold"),
       width=15, command=login).pack(pady=10)

Button(root, text="SIGN UP", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
       width=15, command=signup).pack(pady=5)

root.mainloop()