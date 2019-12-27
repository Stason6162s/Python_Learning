import psycopg2

conn = psycopg2.connect(database='marelli', user='postgres', password='root', host='localhost', port=5432)

cur = conn.cursor()
cur.execute('select fld_series, fld_chassis, fld_wic from tbl_wip;')
result = cur.fetchall()
for item in result:
    print(f'result: {item}')
