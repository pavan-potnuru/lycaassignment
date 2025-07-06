import sqlite3

def run_sql(db_path, sql):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Some problem occured while executing the query: {e}")
        return 0