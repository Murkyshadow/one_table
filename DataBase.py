import sqlite3


class DataBase:
    def __init__(self):
        name = "shop.db"
        self.db = sqlite3.connect(f"{name}")
        cur = self.db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Shop (
            id integer primary key,
            name TEXT,
            address TEXT
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Product (
            id integer primary key,
            product TEXT,
            cost INT,
            id_shop INT
            )
       """)

        self.db.commit()
        cur.close()

    def get_from_shop(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Shop""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_product(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Product""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_shop(self):
        cur = self.db.cursor()
        cur.execute("""SELECT id, name FROM Shop""")
        records = cur.fetchall()
        l = []
        for i in records:
            l.append(str(i[0])+' '+i[1])
        cur.close()
        return l

    def add_in_shop(self, name, ad):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Shop VALUES (NULL, ?, ?)", (name, ad))
        self.db.commit()
        cur.close()

    def add_in_product(self, product, cost, id_shop):
        id_shop = int(id_shop)
        cur = self.db.cursor()
        cur.execute("INSERT INTO Product VALUES (NULL, ?, ?, ?)", (product, cost, id_shop))
        self.db.commit()
        cur.close()

    def delete_from_shop(self, id):
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Shop WHERE id={id}""")
        cur.execute(f"""SELECT COUNT(id) FROM Product WHERE id_shop={id}  """)
        records = cur.fetchall()
        for i in range(records[0][0]):
            self.delete_from_product2(id)
        self.db.commit()
        cur.close()

    def delete_from_product2(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Product WHERE id_shop={id}""")
        self.db.commit()
        cur.close()

    def delete_from_product(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Product WHERE id={id}""")
        self.db.commit()
        cur.close()

    def update_shop(self, id, name, address):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f""" UPDATE Shop set name="{name}", address="{address}" WHERE id={id}""")
        self.db.commit()
        cur.close()

    def update_product(self, id, name, cost, id_shop):
        id = int(id)
        cost = int(cost)
        id_shop = int(id_shop)
        cur = self.db.cursor()
        cur.execute(f""" UPDATE Product set product="{name}", cost="{cost}", id_shop={id_shop} WHERE id={id}""")
        self.db.commit()
        cur.close()


if __name__ == "__main__":
    db = DataBase()
    # db.delete_from_shop()
    # db.update_shop(1, "ПЯТЁРОЧКА")
    db.add_in_shop("12sd3", 'asd')
    rec = db.get_from_shop()
    print(rec)
