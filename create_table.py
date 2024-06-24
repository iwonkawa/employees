import sqlite3
from sqlite3 import Error
from contextlib import contextmanager

@contextmanager
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        yield conn
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def execute_sql(conn, sql):

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_employees_sql = """
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        salary DECIMAL(10, 2)
    );
    """

    create_department_sql = """
    CREATE TABLE IF NOT EXISTS department (
        employee_id INTEGER,
        last_name VARCHAR(50),
        department VARCHAR(50),
        FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
    );
    """

    db_file = "employees.db"

    with create_connection(db_file) as conn:
        if conn is not None:
            execute_sql(conn, create_employees_sql)
            execute_sql(conn, create_department_sql)
            conn.close()