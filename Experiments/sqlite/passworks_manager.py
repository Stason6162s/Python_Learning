import base64
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
        data = bytes(data, 'utf-8')
        encrypted_data = base64.b64encode(data)
        print(encrypted_data)
        return encrypted_data

    @staticmethod
    def decrypts(data):
        decrypted_data = base64.b64decode(data).decode('utf-8')
        return decrypted_data


if __name__ == '__main__':
    sql = SQLiteServer()
    operation_list = sql.get_data('passwrds')
    for i in operation_list:
        print(i)
    print()
    cipher = DataEncrypt()
    test_data = '4v$*RxNe'
    encrypted_txt = cipher.encrypts(test_data)
    decrypted_txt = cipher.decrypts(encrypted_txt)
    print(test_data, encrypted_txt, decrypted_txt)
