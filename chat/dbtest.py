import sqlite3

def Main():
    try:
        con  = sqlite3.connect('pythonpractise.db')
        cur =con.cursor()
        cur.executescript("""
            INSERT INTO people VALUES ("Hassan","xys");
            INSERT INTO people VALUES ("Fatima","adcb");
            INSERT INTO people VALUES ("Faraz","eeee");
        """)

        #
        # cur.execute('CREATE TABLE people (first_name text NOT NULL,last_name text NOT NULL);')
        # cur.execute('INSERT INTO people VALUES ("Hassan","shafiq");')
        # cur.execute('INSERT INTO people VALUES ("Fatima","karim");')
        # cur.execute('INSERT INTO people VALUES ("Faraz","rana");')
        # cur.execute('INSERT INTO people VALUES ("Usman Khn","kukarrr");')
        # table_values = (
        #     ("hasni", "nomi"),
        #     ("nomi", "waqar"),
        #     ("world", "hello")
        # )
        # cur.executemany("INSERT INTO people VALUES (?,?)", table_values)
        con.commit()
        cur.execute('SELECT * FROM people')
        data = cur.fetchall()
        for row in data:
            print('DATA from DB..',row)
    except sqlite3.Error:
        if con:
            print('ERROR rolling back')
            con.rollback()
    finally:
        con.close()

if __name__ == '__main__':
    Main()