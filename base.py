import sqlite3

class SQL:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    #добавление пользователя в бд
    def add_user(self, id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (id) VALUES(?)", (id,))
    #проверка, есть ли пользователь в бд
    def user_exist(self, id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchall()
            return bool(len(result))
    #получить статус пользователя
    def get_status(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[1])
    #обновить статус пользователя
    def update_status(self, id, status):
         with self.connection:
             return self.cursor.execute("UPDATE users SET status = ? WHERE id = ?", (status, id))

    def get_balance(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[2])

    def update_balance(self, id, balance):
         with self.connection:
             return self.cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (balance, id))

    def add_item(self, name, price):
        with self.connection:
            return self.cursor.execute("INSERT INTO items (name, price) VALUES(?,?)", (name, price))

    def get_id_item(self, name):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM items WHERE name = ?", (name,)).fetchone()
            return(result[0])
    
    def get_admin(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[3])

    def get_item(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
            return(result)

    def get_items(self, status):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM items WHERE status = ?", (status,)).fetchall()
            return(result)

    

    #BASKET
    def add_order(self, id_user, id_item):
        with self.connection:
            return self.cursor.execute("INSERT INTO basket (id_user, id_item) VALUES(?,?)", (id_user, id_item))
    
    def get_count(self, id_item, id_user, status):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM basket WHERE id_item = ? AND id_user = ? AND status = ?", (id_item, id_user, status)).fetchone()
            if result:
                return(result[3])
            else:
                return 0

    def update_count(self, id_item, id_user, count, status):
         with self.connection:
             return self.cursor.execute("UPDATE basket SET count = ? WHERE id_item = ? AND id_user = ? AND status = ?", (count, id_item, id_user, status))

    def delete_order(self, id_user, id_item):
        with self.connection:
            return self.cursor.execute("DELETE FROM basket WHERE id_item = ? AND id_user = ? AND status = 0", (id_item, id_user))

    def get_basket(self, id_user, status):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM basket, items WHERE basket.id_user = ? AND basket.status = ? AND basket.id_item = items.id", (id_user, status)).fetchall()
            return result

    def update_status_order(self, id, status):
        with self.connection:
            self.cursor.execute("UPDATE basket SET status = ? WHERE id = ?", (status, id))









    def get_hallway1(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return result[3]

    def get_hallway2(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return result[4]

    def get_hallway3(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return result[5]

    def update_hallway1(self, id, hallway1):
        with self.connection:
            self.cursor.execute("UPDATE users SET hallway1 = ? WHERE id = ?", (hallway1, id))


    def update_hallway2(self, id, hallway2):
        with self.connection:
            self.cursor.execute("UPDATE users SET hallway2 = ? WHERE id = ?", (hallway2, id))


    def update_hallway3(self, id, hallway3):
        with self.connection:
            self.cursor.execute("UPDATE users SET hallway3 = ? WHERE id = ?", (hallway3, id))


    def get_axe(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return (result)


    def update_axe(self, id, axe):
        with self.connection:
            self.cursor.execute("UPDATE users SET axe = ? WHERE id = ?", (axe, id))

    def get_knife(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return result[6]


    def get_paperclip(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return result[7]

    def update_knife(self, id, knife):
        with self.connection:
            self.cursor.execute("UPDATE users SET knife = ? WHERE id = ?", (knife, id))


    def update_paperclip(self, id, paperclip):
        with self.connection:
            self.cursor.execute("UPDATE users SET paperclip = ? WHERE id = ?", (paperclip, id))
    

    
    def close(self):
        self.connection.close()
