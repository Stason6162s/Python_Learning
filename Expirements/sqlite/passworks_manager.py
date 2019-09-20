import sqlite3


class SQLiteServer:
    """
    Class work with the SQLite data bases
    """
    connection = sqlite3.connect('pass_mgr.db')
    cursor = connection.cursor()

    def get_data(self, table):
        conn = self.connection
        cursor = self.cursor
        try:
            cursor.execute(f"select * from {table} ")
            result = cursor.fetchall()
            conn.commit()
            return result
        except sqlite3.OperationalError as exc:
            print(exc)

    def insert_data(self, data):
        pass


class DataEncrypt:
    """
    Encrypt/Decrypt data in table
    """

    @staticmethod
    def encrypts(data):
        pass

    @staticmethod
    def decrypts(data):
        pass


if __name__ == '__main__':
    sql = SQLiteServer()
    operation_list = sql.get_data('passwrds')

    for i in operation_list:
        print(i)
