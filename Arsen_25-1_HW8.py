import sqlite3


def create_connection(db_hw):
    conn = None
    try:
        conn = sqlite3.connect(db_hw)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


create_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''


def add_products(conn, products):
    try:
        sql = '''INSERT INTO products(product_title, quantity, price ) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        for i in products:
            cursor.execute(sql, i)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_products_price(conn, new_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, new_price)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_quantity(conn, new_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, new_quantity)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, products_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (products_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def find_products(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        for i in cursor.fetchall():
            print(i)
    except sqlite3.Error as e:
        print(e)


def search_products(conn, products):
    try:
        sql = """SELECT * FROM products WHERE product_title LIKE ?"""
        cursor = conn.cursor()
        cursor.execute(sql, (f'%{products}%',))
        for i in cursor.fetchall():
            print(i)
    except sqlite3.Error as e:
        print(e)


products_list = [('апельсин', 5, 200.00), ('арбуз', 10, 15.00), ('слива', 40, 75.00), ('банан', 70, 120.00),
                 ('капуста', 80, 20.00), ('мыло', 100, 30.00), ('фери', 200, 140.00), ('шампунь', 300, 150.00),
                 ('пена', 120, 220.00), ('бритва', 400, 20.00), ('чай', 40, 70.00), ('кофе', 30, 130.00),
                 ('сахар', 300, 60.00), ('конфеты', 300, 450.00), ('молоко', 40, 80.00)]

database = 'hw.db'
connect = create_connection(database)

if connect is not None:
    search_products(connect, 'мыло')
    print('Done')
    connect.close()
