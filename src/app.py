from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    search = request.args.get('search', '').strip()
    department = request.args.get('department', '').strip()
    conn = get_db_connection()

    query = 'SELECT * FROM employees WHERE 1=1'
    params = []
    if search:
        query += ' AND (name LIKE ? OR emp_id LIKE ? OR designation LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%', f'%{search}%'])
    if department:
        query += ' AND department = ?'
        params.append(department)

    query += ' ORDER BY id DESC'
    employees = conn.execute(query, params).fetchall()

    dept_rows = conn.execute('SELECT DISTINCT department FROM employees WHERE department IS NOT NULL AND department != ""').fetchall()
    departments = [r['department'] for r in dept_rows]

    all_emps = conn.execute('SELECT salary, status, department FROM employees').fetchall()
    total_employees = len(all_emps)
    active_employees = sum(1 for e in all_emps if e['status'] == 'Active')
    total_departments = len(set(e['department'] for e in all_emps))
    total_payroll = sum(e['salary'] for e in all_emps)
    conn.close()

    return render_template('index.html', employees=employees, departments=departments, search_query=search, selected_department=department, total_employees=total_employees, active_employees=active_employees, total_departments=total_departments, total_payroll=total_payroll)

@app.route('/add', methods=['POST'])
def add_employee():
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO employees (emp_id, name, email, department, designation, salary, status) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (request.form['emp_id'], request.form['name'], request.form['email'], request.form['department'], request.form['designation'], float(request.form['salary']), 'Active'))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_employee(id):
    conn = get_db_connection()
    conn.execute('UPDATE employees SET name = ?, department = ?, designation = ?, salary = ?, status = ? WHERE id = ?',
                 (request.form['name'], request.form['department'], request.form['designation'], float(request.form['salary']), request.form['status'], id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
