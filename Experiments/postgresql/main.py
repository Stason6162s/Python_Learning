from datetime import datetime

import psycopg2

current_time = datetime.now().strftime("%H:%M:%S")
print(f"Hi, there! Start is {current_time}")

conn = psycopg2.connect(database='marelli_4m', user='postgres', password='root', host='localhost', port=5432)
cur = conn.cursor()


def get_records():
    query = 'select date, station, description, m.name, us.name from records rec left join ' \
            'users us on us.id=rec.user_id left join m_types m on rec.type_m = m.id order by rec.date desc;'
    cur.execute(query)
    result = cur.fetchall()
    for item in result:
        print(item)


def insert_rec():
    insert_string = f"INSERT INTO records(date, shop, station, model, description, type_m, user_id, actions, status)" \
                    f"VALUES (current_date," \
                    f"'CPM', 'CO-6', 'All', 'Description', 2, 3, 'None', 'Confirm');"
    cur.execute(insert_string)


if __name__ == '__main__':
    # insert_rec()
    get_records()
