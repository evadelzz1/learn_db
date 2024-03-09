import sqlite3

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "insert into student(name, mobile) values (?,?)"
    rows = cur.execute(sql, ('김삼순', None))
    
    conn.commit()

