#functions related to the changes in schema of the DB

import sqlite3

conn = sqlite3.connect('hn.db')
cur = conn.cursor()

def schema_update_1():
    cur.execute('CREATE TABLE posts(Post_ID PRIMARY KEY, Title, Story_Text, Creation_date, Num_Comments);')







conn.close()
