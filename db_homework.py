import sqlite3

con = sqlite3.connect('db_1.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL, email TEXT UNIQUE) ''')

cursor.execute('''CREATE TABLE orders(id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER, product_id INTEGER, quantity INTEGER,FOREIGN KEY(user_id) REFERENCES user(id),
FOREIGN KEY(product_id) REFERENCES products(id) )''')

cursor.execute('''CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
price REAL)''')

cursor.execute("INSERT INTO users (name,email) VALUES(?,?)",('Егор Летов','letov@mail.com'))
cursor.execute("INSERT INTO users (name,email) VALUES(?,?)",('Константин Кинчев','kinchev@mail.com'))
cursor.execute("INSERT INTO users (name,email) VALUES(?,?)",('Александр Васильев','splin@mail.com'))

cursor.execute("INSERT INTO products (name,price) VALUES(?,?)",('iPhone',700))
cursor.execute("INSERT INTO products (name,price) VALUES(?,?)",('Samsung',1000))
cursor.execute("INSERT INTO products (name,price) VALUES(?,?)",('Pixel7',350.50))

cursor.execute("INSERT INTO orders (user_id,product_id,quantity) VALUES(?,?,?)",(1,1,1))
cursor.execute("INSERT INTO orders (user_id,product_id,quantity) VALUES(?,?,?)",(2,2,1))
cursor.execute("INSERT INTO orders (user_id,product_id,quantity) VALUES(?,?,?)",(3,3,2))

con.commit()

cursor.execute("SELECT users.name, products.name, orders.quantity FROM users "
               "JOIN orders ON users.id = orders.user_id "
               "JOIN products ON products.id = orders.product_id")
rows = cursor.fetchall()

for row in rows:
    print(row)

con.close()
