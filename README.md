
Description

This project is a simple user registration and database management system implemented using Python's Tkinter library for the graphical user interface (GUI) and SQLite for database operations. 
It allows users to sign up with their credentials, and it provides an interface to manage the stored user data.

Features

User registration with username, age, email, and password.
Data validation for age and email format.
Secure storage of user data in an SQLite database.
GUI for displaying and managing user data.
Options to delete all data or remove specific user data.

Requirements

Python 3.x
Tkinter library (usually included with Python)
SQLite3 library (usually included with Python)

Installation

Clone the repository or download the Database_Result.py and Database_registration.py files.
Ensure you have Python installed on your system. You can download it from python.org.

How to Run

Running the Registration Form
Open a terminal or command prompt.
Navigate to the directory where the Database_registration.py file is located.
Run the following command:
bashCopy
python Database_registration.py
Fill in the registration form and click "Sign Up" to register a new user.
Running the Database Management Interface
Open a terminal or command prompt.
Navigate to the directory where the Database_Result.py file is located.

Run the following command:
bashCopy
python Database_Result.py
The interface will display the current user data. You can delete all data or remove specific user data using the provided options.
Usage

Registration Form

Enter your username, age, email, and password in the respective fields.
Click the "Sign Up" button to register.
If any field is invalid or missing, an error message will be displayed.
If the username already exists, you will be prompted to choose a different username.
Database Management Interface
The interface displays all registered users.
Click the "Delete All Data" button to clear all user data (confirmation required).
Enter a username in the provided field and click "Remove specific Data" to delete a specific user.

Code Structure

Database_registration.py
validate_age(age): Validates the age input.
validate_email(email): Validates the email format using regular expressions.
existing_user(username): Checks if a username already exists in the database.
table(): Creates the users table in the SQLite database if it doesn't exist.
sign_up(): Handles the user registration process, including data validation and insertion into the database.
Database_Result.py
data(): Fetches all user data from the database.
clrall(): Deletes all user data from the database.
spc(username): Deletes a specific user from the database based on the username.
display(): Displays the user data in a GUI window and provides options to delete data.

