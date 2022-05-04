import sqlite3


class DataBase:
    def __init__(self):     # create
        name = "shop.db"
        self.db = sqlite3.connect(f"{name}")
        cur = self.db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Shop (
            id integer primary key,
            name TEXT,
            address TEXT
            )
        """)

        self.db.commit()
        cur.close()

    def get_from_shop(self):    # read
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Shop""")
        records = cur.fetchall()
        cur.close()
        return records

    def update_shop(self, id, name, address):   # update
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f""" UPDATE Shop set name="{name}", address="{address}" WHERE id={id}""")
        self.db.commit()
        cur.close()

    def delete_from_shop(self, id):     # delete
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Shop WHERE id={id}""")
        self.db.commit()
        cur.close()

    def add_in_shop(self, name, address):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Shop VALUES (NULL, ?, ?)", (name, address))
        self.db.commit()
        cur.close()
