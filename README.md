# group_activity

# 🧠 User Info Program

## 📘 Project Overview
This group project is a simple **Python program** organized into **four separate files**.  
It collects and validates user information (name and age), converts them into **binary format**, creates a personalized message, and saves/reads it from a text file — all while handling errors gracefully.

---

## 🗂️ Project Structure

user_info_program/
├── helper_functions.py
├── file_manager.py
├── greetings.py
├── main_program.py
└── README.md

yaml
Copy code

---

## ⚙️ File Descriptions

### 1. `helper_functions.py`
Contains the core logic of the program.

**Functions:**
- **validate_input(user_input)** → Checks if input is not empty and returns True/False.  
- **convert_to_binary(text)** → Converts name or age to binary format using ASCII or `bin()`.  
- **create_message(name, age, name_binary, age_binary)** → Builds a personalized message.

---

### 2. `file_manager.py`
Handles file saving and reading with error handling.

**Functions:**
- **save_message(message)** → Saves message to `user_message.txt` and confirms success.  
- **read_message()** → Reads and displays saved message, handles missing file errors.

---

### 3. `greetings.py`
Displays user-friendly messages before and after the program runs.

**Functions:**
- **show_intro()** → Prints program introduction.  
- **show_exit_message()** → Prints goodbye message.

---

### 4. `main_program.py`
Controls program flow and connects all other files.

**Main Flow:**
1. Imports functions from the other files.  
2. Defines `get_user_info()` to collect valid name and age.  
3. Converts inputs to binary using helper functions.  
4. Creates and displays the personalized message.  
5. Saves the message and reads it back from the file.  
6. Ends with a farewell message.

---

## 🧩 Example Output

==============================
Welcome to the User Info Program
Enter your name:
Invalid name! Please try again.
Enter your name: Herve
Enter your age: hi
Invalid age! Please enter a number.
Enter your age: 23

Hello Herve, you are 23 years old!
Name in binary: 01001000 01100101 01110010 01110110 01100101
Age in binary: 0b10111

Message saved successfully.
Reading saved message...
Hello Herve, you are 23 years old!
Name in binary: 01001000 01100101 01110010 01110110 01100101
Age in binary: 0b10111

Thank you for using the program. Goodbye!

yaml
Copy code

---

## 🚀 How to Run the Program

1. Open your terminal.  
2. Navigate to your project folder:
   ```bash
   cd user_info_program
Run the main file:

bash
Copy code
python3 main_program.py
🧑‍💻 Collaborators
Name	Role	Student ID (if applicable)
Olivier Dusabamahoro	Developer & Documentation Lead	—
[Add Collaborator Name 1]	Logic and Validation Developer	—
[Add Collaborator Name 2]	File Handling and Testing	—
[Add Collaborator Name 3]	UI & Message Design	—

✨ Each collaborator contributed to different sections such as input validation, binary conversion, file handling, and user interface design.

🛠️ Technologies Used
Python 3

File handling (open, try-except)

String and binary manipulation

Modular programming (imports and function calls)

💡 Learning Outcomes
Through this project, we practiced:

Dividing a program into multiple files.

Using functions for modular and reusable code.

Handling user input and validation.

Managing file read/write operations.

Collaborating as a team on a shared coding task.

📄 License
This project is open for educational use only.
© 2025 ALU Group Project.
