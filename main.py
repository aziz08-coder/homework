import sqlite3

db= sqlite3.connect("itproger.db")

c=db.cursor()

# c.execute(""" CREATE TABLE articles(
#         title text,
#         full_text text,
#           views integer,
#         avtor text
# )
          
# """)

c.execute("INSERT INTO articles VALUES('Fasbook is cool', 'Fasbook is most',400,'Eliiz')")

# c.execute(" SELECT rowid,title FROM articles")
# print(c.fetchmany(2))

db.commit()

db.close()