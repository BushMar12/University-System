# University Management System

A **MVC-based** university student management system supporting both **Command Line Interface (CLI)** and **Graphical User Interface (GUI)**. It provides features for student registration, login, course enrollment, course removal, subject viewing, and administrator operations.

---

## ✨ Features

✅ Student registration and login  
✅ Maximum of 4 enrolled subjects per student  
✅ Automatic generation of subject marks and grades (HD/D/C/P/Z)  
✅ Students can view or remove enrolled subjects  
✅ Administrator functions:
- Clear the student database
- Group students by grade
- Partition students by pass/fail
- Remove student by ID
- Display all students

✅ **Colored CLI output (ANSI color codes)** 
✅ **GUI interface (built with Tkinter)**

---

## 🏗️ Project Structure

```bash
├── app.py                 # Main entry point
├── controllers/
│   ├── admin_controller.py
│   ├── student_controller.py
│   └── subject_controller.py
├── models/
│   ├── student.py
│   ├── database.py
│   └── subject.py
├── views/
│   ├── cli_view.py
│   └── gui_view.py
├── students.data          # Student data file (pickle format)
```

------

## 🚀 How to Run

### 1️⃣ **Run CLI Interface**

```bash
python app.py
```

When prompted, enter `C` (CLI) to launch the command-line version.

👉 CLI uses **ANSI color codes**; recommended to run in a terminal or command prompt supporting colors.

------

### 2️⃣ **Run GUI Interface**

```bash
python app.py
```

When prompted, enter `G` (GUI) to launch the graphical interface.

Alternatively, run directly:

```bash
python views/gui_view.py
```

------

## ⚙️ Requirements

✅ Python 3.7+
✅ Tkinter (included in Python standard library)

For Linux, if Tkinter is missing:

```bash
sudo apt-get install python3-tk
```

(Windows and macOS usually have it pre-installed)

------

## 📚 Data Storage

Student data is saved in `students.data` (pickle format).
 Deleting or clearing this file will result in loss of stored data.

The admin's "clear database" option will also reset this file.

------

## 📝 Author

Developed by Group 4

------

## 🧩 Notes

✅ Supports running both CLI and GUI concurrently (multithreaded)
✅ CLI color output works on **Linux / macOS / Windows Terminal / VSCode Terminal**

⚠️ If colors do not display properly in Windows Command Prompt, try using **Windows Terminal / PowerShell / VSCode Terminal**