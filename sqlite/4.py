import sqlite3

conn = sqlite3.connect("test.db")

data = (
    (21, '010-5555-5555'),
    (22, '010-6666-6666')
)

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values (?,?)"
    rows = cur.executemany(sql, data)
    
    conn.commit()


with conn:
    cur = conn.cursor()
    sql = "select * from student where id=? or id=?"
    rows = cur.execute(sql, (22, 23))

    for row in rows:
        print(row)

