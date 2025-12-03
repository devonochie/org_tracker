# 🏢 Organization Data Tracker (CLI)

A **Python-based command-line application** for managing organizational data, including **organizations, departments, and employees**, using a **relational MySQL database**.

## 🎯 Project Purpose

The goal of this project is to:
- Learn **how Python interacts with a real database**
- Understand **relational data modeling**
- Practice **clean backend code structure**
- Build foundations for future automation and AI systems

This project intentionally avoids web frameworks and UI complexity to focus on **core backend fundamentals**.

---

## 🧠 Concepts Covered

- Python command-line applications
- MySQL relational databases
- Primary and foreign keys
- One-to-many relationships
- SQL execution from Python
- Data integrity with constraints
- Basic bulk data insertion

---

## 🧱 Tech Stack

- **Python 3.11+**
- **MySQL Server**
- **MySQL Workbench**
- `mysql-connector-python`
- Terminal / Command Prompt

---

## 📁 Project Structure

org_tracker/
│
├── db/
│ ├── connection.py
│ └── schema.sql
│
├── services/
│ ├── organization_service.py
│ ├── department_service.py
│ └── employee_service.py
│
├── cli/
│ └── main.py
│
├── migrations.py
└── README.md

markdown
Copy code

This structure mirrors **real backend projects** in an intentionally simple form.

---

## 🗄️ Database Design

### Entities

#### Organizations
Represents a company or institution.
- `id`
- `name`
- `country`
- `created_at`

#### Departments
Each department belongs to one organization.
- `id`
- `organization_id`
- `name`
- `created_at`

#### Employees
Each employee belongs to one department.
- `id`
- `department_id`
- `name`
- `email`
- `created_at`

The database enforces **referential integrity** using foreign keys.

---

## ▶️ Running the Project

### 1️⃣ Install dependencies
```bash
pip install mysql-connector-python
2️⃣ Create the database
Open MySQL Workbench, create a new SQL tab, and run:

Verify the database and tables exist.

3️⃣ Configure database connection
Edit config.py:
4️⃣ Run the CLI app
From the project root:

python -m cli.main
You should see the interactive menu.

💻 CLI Features (MVP)
Create organizations

List organizations

Add departments to organizations

List departments by organization

(Optional) Add employees to departments

Bulk organization insertion

