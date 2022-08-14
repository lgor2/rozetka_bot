import sqlite3


db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute('''
CREATE TABLE IF NOT EXISTS status(

id INTEGER PRIMARY KEY AUTOINCREMENT,
status TEXT NOT NULL

);''')

sql.execute('''CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,
telegram_id INTEGER UNIQUE NOT NULL,
status_id TEXT NOT NULL,
FOREIGN KEY (status_id) REFERENCES status (id)

);''')

sql.execute('''CREATE TABLE IF NOT EXISTS wait(

id INTEGER PRIMARY KEY AUTOINCREMENT,
word_wait TEXT NOT NULL,
user_id INTEGER UNIQUE NOT NULL,
FOREIGN KEY (user_id) REFERENCES users (id)

);''')

sql.execute('''CREATE TABLE IF NOT EXISTS product(

id INTEGER PRIMARY KEY AUTOINCREMENT,
photo BLOB NOT NULL,
name TEXT NOT NULL,
price INTEGER NOT NULL,
reason_for_markdown TEXT,
link TEXT NOT NULL

);''')

db.commit()
