import sqlite3


def new_user(telegram_id):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()

    c.execute('''INSERT INTO users (telegram_id, status_id)
                VALUES(?, ?)''', (telegram_id, 1))

    conn.commit()
    conn.close()


def change_status_user(telegram_id, status_id):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()

    c.execute('''UPDATE users SET status_id = ? WHERE telegram_id = ?''', (status_id, telegram_id))

    conn.commit()
    conn.close()


def delete_user(telegram_id):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()

    c.execute('''DELETE FROM users WHERE telegram_id = ?''', (telegram_id,))

    conn.commit()
    conn.close()


def new_products(lists_of_values):
    """Arguments is an array of lists [[link_to_photo, name, price, reason_for_markdown, link], ...]"""

    conn = sqlite3.connect('server.db')
    c = conn.cursor()

    for i in range(len(lists_of_values)):
        c.execute('''INSERT OR IGNORE INTO products (link_to_photo, name, price, reason_for_markdown, link)
                        VALUES(?, ?, ?, ?, ?)''', (lists_of_values[i]))

    conn.commit()
    conn.close()


def delete_all_products():
    conn = sqlite3.connect('server.db')
    c = conn.cursor()

    c.execute('''DELETE FROM products;''')

    conn.commit()
    conn.close()


# new_user(1)
# new_user(2)
# new_user(3)
#
# change_status_user(1, 111)
# change_status_user(3, 333)
#
# delete_user(2)

# many_goods = [['link_TO_photo1', 'NAME', 100, 'После тестирования', 'lliinnkk1'],
#               ['link_TO_photo2', 'NAME', 100, 'После тестирования', 'lliinnkk2'],
#               ['link_TO_photo3', 'NAME', 100, 'После тестирования', 'lliinnkk3']]
#
# new_products(many_goods)