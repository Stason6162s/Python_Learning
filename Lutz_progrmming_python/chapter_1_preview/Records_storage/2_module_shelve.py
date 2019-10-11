import shelve

from Lutz_progrmming_python.chapter_1_preview.Records_storage.init_data import anton, jonie, andrm

db_name_shelve = 'people-shelve'


def make_db_shelve():
    data_base = shelve.open(db_name_shelve)
    data_base['anton'] = anton
    data_base['jonie'] = jonie
    data_base.close()


def dump_db_shelve():
    data_base = shelve.open(db_name_shelve)
    for key in data_base:
        print(f'{key} => {data_base[key]}')
    data_base.close()


def update_db_shelve():
    data_base = shelve.open(db_name_shelve)
    antony = data_base['anton']
    antony['job'] = "Technician alkash"
    data_base['anton'] = antony
    data_base['andrm'] = andrm
    data_base.close()


if __name__ == '__main__':
    make_db_shelve()
    dump_db_shelve()
    update_db_shelve()
    dump_db_shelve()
