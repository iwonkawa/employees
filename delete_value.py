import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def delete_where(conn, table, **kwargs):

    # Construct WHERE clause dynamically
    conditions = " AND ".join([f"{key} = ?" for key in kwargs])
    values = tuple(kwargs.values())

    sql = f"DELETE FROM {table} WHERE {conditions}"
    
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print(f"Deleted rows from {table} where {conditions}")
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    conn = create_connection("employees.db")
    if conn is not None:
        delete_where(conn, "employees", last_name="Doe")
        conn.close()
    else:
        print("Error! Cannot create the database connection.")