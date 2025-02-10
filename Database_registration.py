from tkinter import *
from tkinter import messagebox 
import sqlite3
import re


root = Tk()
root.title("Signup Form")
root.geometry('250x175')
root.configure(bg='sky blue')


username_label=Label(root,text='USERNAME', fg='black').grid(row=0)
username_entry=Entry(root)
username_entry.grid(row=0, column=1)



age_label = Label(root, text='AGE', fg='black').grid(row=1)
age_entry = Entry(root)
age_entry.grid(row=1,column=1)


email_label = Label(root, text='EMAIL', fg='black').grid(row=2)
email_entry = Entry(root)
email_entry.grid(row=2,column=1)


password_label = Label(root, text='PASSWORD', fg='black').grid(row=3)
password_entry = Entry(root, show='*')
password_entry.grid(row=3,column=1)


def validate_age(age):
    try:
        age=int(age)
        if age<=0 or age>150:
            return False
        return True

    except:
        print("Error")
    
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def existing_user(username):
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False
    
    
def table():
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, age INT, email TEXT, password TEXT)')
    conn.commit()
    conn.close()


def sign_up():
    username = username_entry.get()
    username=username.lower()
    age = age_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not username or not age or not email or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address")
        return
    if not validate_age(age):
        messagebox.showerror("Error", "Please enter a valid age address")
        return

    if existing_user(username):
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return
    
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(username, age, email, password) VALUES (?, ?, ?, ?)', (username, age, email, password))
    conn.commit()
    conn.close()


    username_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


    messagebox.showinfo("Success", "Signup Successful!")


button = Button(root, text='Sign Up',bg='green', command=sign_up)
button.grid(row=4,column=1)

def reg():
    exit()


button1 = Button(root,text='Registration Complete',bg='red', command=reg)
button1.grid(row=5,column=1)

table()

root.mainloop()
