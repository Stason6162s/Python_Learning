import pyodbc


class Car:
    def __init__(self, series, chassis):
        self.series = series
        self.chassis = chassis
        self.name = series + chassis

    def __str__(self):
        return self.name

    def info(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s = %s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def get_wic(self):
        pass


if __name__ == '__main__':
    cars = []
    query = "SELECT fld_series, fld_chassis,fld_sequence_number, fld_status FROM dbo.tbl_wip " \
            " where fld_series != 'R521' AND fld_sequence_number>'201701010001'  ORDER BY fld_sequence_number DESC "
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=eu-s-ru-sql1;DATABASE=cpm1;UID=cpmread;PWD=reader13')
    cursor = conn.cursor()
    cursor.execute(query)
    result_set = cursor.fetchall()
    for rec in result_set:
        # car = '%s%s' % (rec[0], rec[1])
        car = Car(rec[0], rec[1])
        cars.append(car)
    for key in cars:
        print(key.info())
