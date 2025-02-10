
import sqlite3
from tkinter import *
import tkinter.messagebox

def data():
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    d_c = c.fetchall()
    conn.close()
    return d_c

def clrall():
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()

def spc(username):
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    conn.close()
    


def display():
    da = data()
    
    root = Tk()
    root.title("Database Content")

    d_text = Text(root, height=20, width=70)
    d_text.pack()
    c=0
    for i in da:
        c+=1
        d_text.insert(END, f"No.{c}\nUsername: {i[0]}, Age: {i[1]}, Email: {i[2]}, Password: {i[3]}\n\n")

    def clear_text():
        confirm = tkinter.messagebox.askyesno("Confirmation", "Are you sure you want to delete all data?")
        if confirm:
            d_text.delete(1.0, END)
            clrall()
    
    clear_button = Button(root, text="Delete All Data", command=clear_text)
    clear_button.pack()


    label=Label(root,text='Enter the usename to remove: ')
    label.pack()

    en=Entry(root)
    en.pack()

    def dell():
        username=en.get()
        if username:
            spc(username)
            d_text.delete(1.0, END)
            da = data()
            c=0
            for i in da:
                c+=1
                d_text.insert(END, f"No.{c}\nUsername: {i[0]}, Age: {i[1]}, Email: {i[2]}, Password: {i[3]}\n\n")
        else:
            tkinter.messagebox.showerror("Error", "Please enter a username.")            
            
        
    button=Button(root,text='Remove specific Data',command=dell)
    button.pack()
    
    root.mainloop()

display()
Title: "User Registration and Database Management System"

Objective of the Project with Highlighting Its Importance:
The objective of this project is to create a user registration system using a graphical interface (GUI) in Python's Tkinter library. 
The system allows users to sign up by providing their username, age, email, and password. 
The importance of this project lies in its practical application for managing user data securely, enabling user authentication, and facilitating data retrieval and management operations.

Methodology:

Signup Form: The signup form GUI captures user input for username, age, email, and password, performing validation checks for data integrity.
Data Validation: Age validation ensures that only valid age values are accepted (between 1 and 150), while email validation checks for a valid email format using regular expressions.
Database Operations: SQLite database operations include creating a user table, inserting new user records, fetching all user data, deleting all data, and removing specific user data based on username.
User Interface: The GUI elements such as labels, entry fields, buttons, and text display areas are designed for a user-friendly experience.

Expected Outcome of the Project:

User Registration: Users can register with unique credentials, and their data is stored securely in an SQLite database.
Data Management: The system allows administrators or authorized users to view all registered users, delete all data (if required), or remove specific users from the database.
Data Integrity: Validation checks ensure that only valid and formatted data is accepted during signup, enhancing data integrity.
Ease of Use: The graphical interface makes it easy for users to interact with the system, promoting a seamless registration experience.

Application of the Project:

Web Development: Similar user registration and data management systems are used in web applications to handle user accounts and profiles securely.
Educational Platforms: Can be used as a learning tool for understanding GUI development, database integration, and data validation techniques.
Small-Scale Databases: Suitable for small-scale applications or projects requiring user authentication and data storage.
Administrative Tools: Useful for administrators or system managers to manage user accounts and perform database operations efficiently.

