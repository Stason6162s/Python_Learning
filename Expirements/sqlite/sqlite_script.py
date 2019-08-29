import sqlite3


class Server:
    conn = sqlite3.connect("config.db")
    cursor = conn.cursor()

    def sqlite_select(self, table):
        cursor = self.cursor
        conn = self.conn
        cursor.execute(f'select* from {table}')
        print(cursor.fetchall())
        conn.commit()

    def sqlite_create_table(self):
        cursor = self.cursor
        conn = self.conn
        try:
            cursor.execute("create table stations (index_num text, pc_name text, sql_number)")
            print('Table create')
            cursor.execute(f"insert into stations values ('CO1', 'eu-st-10010', '93')")
            conn.commit()
            print('The first string inserts')
            stations = [('CO2', 'eu-st-10002', '3'), ('CO3', 'eu-st-10039', '4'), ('CO4', 'eu-st-10010', '5'), ]
            cursor.executemany('insert into stations values(?,?,?)', stations)
            conn.commit()
            print('A many strings insert')
        except sqlite3.OperationalError as exc:
            print(exc.args[0])


if __name__ == '__main__':
    sql = Server()
    sql.sqlite_select('models')
