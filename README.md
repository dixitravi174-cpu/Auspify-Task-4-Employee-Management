# Task 4: Employee Management System

A web-based Employee Management System built using **Python (Flask)** and **SQLite3** for the Auspify Technologies Software Development Internship.

---

## 📌 Project Overview
This application manages employee records, department-wise filtering, salary rollups, active staff tracking, and instant payroll calculations through an interactive reporting dashboard.

### ✨ Key Features
- **Reports Dashboard (KPIs)**: Real-time tracking of Total Employees, Active Staff Count, Total Departments, and Total Monthly Payroll (₹).
- **Employee Registration**: Register staff with unique Employee ID, Full Name, Email Address, Department, Designation, and Salary.
- **Search & Dynamic Filter**: Search employees dynamically by Name, Emp ID, or Designation and filter records by Department.
- **Inline Updates & Status Control**: Modify employee details, salaries, and employment status (`Active` / `On Leave`) directly from the table.
- **Delete Records & Instant Recalculation**: Remove obsolete employee records with instant payroll and KPI metric recalculation.
- **Persistent Storage**: Lightweight SQLite3 database (`employee.db`).

---

## 🛠️ Tech Stack
- **Backend**: Python 3.12, Flask
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2 Templates

---

## 🚀 How to Run Locally

1. **Navigate to project directory:**
   ```bash
   cd Task_4_Employee_Management