import sqlite3

def create_connection(db_file):
    """ 
    Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def update(conn, table, employee_id, **kwargs):

    columns = ", ".join(f"{k}=?" for k in kwargs.keys())
    values = list(kwargs.values())
    values.append(employee_id)
    sql = f"UPDATE {table} SET {columns} WHERE employee_id=?"
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

if __name__ == "__main__":

    conn = create_connection("employees.db")
    update(conn, "department", 5, department="IT", last_name="Wilson")
    update(conn, "department", 5, department="Logistics")

    # Close the connection
    conn.close()