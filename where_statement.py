import sqlite3

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def select_where(conn, employees, salary=55000):

    cur = conn.cursor()
    sql = f"SELECT * FROM {employees} WHERE salary >= ?"
    cur.execute(sql, (salary,))
    rows = cur.fetchall()
    return rows

if __name__ == "__main__":
    # Example usage:
    conn = create_connection("employees.db")
    if conn is not None:
        # Example: Query employees with salary >= 55000
        employees_table = "employees"  # Assuming this is your table name
        query_result = select_where(conn, employees_table, salary=55000)
        for row in query_result:
            print(row)
        
        conn.close()
    else:
        print("Error! Cannot create the database connection.")