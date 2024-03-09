import sqlite3

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "select * from student where id=? or name=?"
    rows = cur.execute(sql, (1, '홍길순'))
    
    for row in rows:
        print(row)
