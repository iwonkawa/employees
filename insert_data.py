import sqlite3

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def add_employee(conn, employees):

    sql = '''INSERT INTO employees(employee_id, first_name, last_name, salary)
        VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.executemany(sql, employees)
    conn.commit()

def add_department(conn, departments):

    sql = '''INSERT INTO department(employee_id, last_name, department)
        VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.executemany(sql, departments)
    conn.commit()

def select_department_by_employee_id(conn, employee_id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM department WHERE employee_id=?", (employee_id,))
    rows = cur.fetchall()
    return rows


if __name__ == "__main__":
    # Define employees
    employees = [
        (1, 'John', 'Doe', 50000.00),
        (2, 'Jane', 'Smith', 60000.00),
        (3, 'Mike', 'Johnson', 55000.00),
        (4, 'Emily', 'Davis', 52000.00),
        (5, 'Chris', 'Wilson', 62000.00)
    ]

    # Define departments
    departments = [
        (1, 'Doe', 'HR'),
        (2, 'Smith', 'IT'),
        (3, 'Johnson', 'Sales'),
        (4, 'Davis', 'Marketing'),
        (5, 'Wilson', 'IT')
    ]

    # Create a database connection
    conn = create_connection("employees.db")

    if conn is not None:
        # Insert employees
        add_employee(conn, employees)

        # Insert departments
        add_department(conn, departments)

        # Example of selecting departments for an employee
        employee_id = 1
        departments = select_department_by_employee_id(conn, employee_id)
        print(f"Departments for Employee ID {employee_id}:")
        for department in departments:
            print(department)

        conn.close()
    else:
        print("Error! Cannot create the database connection.")