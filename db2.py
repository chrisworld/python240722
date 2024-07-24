
import sqlite3

con = sqlite3.connect(r"c:\work\sample.db")


cur = con.cursor()

cur.execute("create table if not exists PhoneBook (Name text, PhoneNum text);")

cur.execute("insert into PhoneBook values('derick', '010-111');")

name = "홍길동"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values(?,?);", (name, phoneNumber))

datalist = (("전씨","010-123"),("박씨","010-456"))
cur.executemany("insert into PhoneBook values(?,?);", datalist)

cur.execute("select * from PhoneBook;")

print(cur.fetchone())
print(cur.fetchmany(2))
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

con.commit()

# for row in cur:
#     print(row)
