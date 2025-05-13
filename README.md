# 📚 Library Management System

A simple web-based Library Management System built using **Flask (Python)** and **MySQL**, allowing users to add, view, edit, and delete book records.

---

## 🚀 Features

- ✅ Add new books with title, author, and publication year
- ✅ View all added books in a tabular format
- ✅ Edit or delete individual book records
- ✅ Toggle visibility of the books table 

---

## 🛠 Tech Stack

| Layer     | Technology          |
|-----------|---------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python (Flask)       |
| Database  | MySQL                |
| ORM       | MySQLdb / pymysql (DB connector) |
| Hosting   | Localhost (can be deployed to AWS/Heroku) |

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management.git
cd library-management
```
### 2. Set up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
### 4. Configure MySQL Database
```bash
CREATE DATABASE library;
USE library;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT
);
```
Note: If you don't have the mysql database, then install it and run the step 4

### 5. Run the project.py file
```bash
python app.py
```

![image](https://github.com/user-attachments/assets/cb440636-a8f5-496c-a3da-d2ae8bbf6c9d)

