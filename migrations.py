#functions related to the changes in schema of the DB

import sqlite3

conn = sqlite3.connect('hn.db')
cur = conn.cursor()


#--------- DB Schema Update Functions ---------


def schema_update_1():
    cur.execute('CREATE TABLE posts(Post_ID PRIMARY KEY, Title, Story_Text, Creation_date, Num_Comments);')

def schema_update_2():
    cur.execute('ALTER TABLE posts ADD created_at_i')

#--------- Updates ---------

#schema_update_1()
schema_update_2()



conn.close()
