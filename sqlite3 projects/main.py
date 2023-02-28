import sqlite3
database = input()
con = sqlite3.connect(database)
cur = con.cursor()
result = cur.execute("""SELECT * FROM Films WHERE (year > 1997) 
and (genre = '7' or genre = '9')""").fetchall()
for elem in result:
    print(elem[1])
con.close()