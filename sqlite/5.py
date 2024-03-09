import sqlite3, random

family_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병볕솥하라")

def make_name():
    sung = random.choice(family_names)
    name = random.sample(first_names, 2)
    print(type(sung), type(name))

    name = "".join(random.sample(first_names, 2))
    #print(type(sung), type(name))
    return(sung + name, )

# print(make_name())
# exit()

data = []
for i in range(0, 100):
    data.append(make_name())

# print(data)
# exit()

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "insert into tt(name) values (?)"
    rows = cur.executemany(sql, data)
    
    conn.commit()
