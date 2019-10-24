import shelve

from Lutz_progrmming_python.chapter_1_preview.OOP.person_alternative import Person, Manager

db_name = 'class-shelve'


def make_db_classes():
    antony = Person('Anton Kobeshev', 32, 60000, 'Techician')
    jonie = Person('Evgeny Zolotuchin', 36, 60000, 'Techician')
    temic = Manager('Artem Surkov', 45, 150000)

    db = shelve.open(db_name)
    db['tony'] = antony
    db['jone'] = jonie
    db['tema'] = temic

    db.close()


def dump_db_classes():
    db = shelve.open(db_name)
    for key in db:
        print(f"{key} => \n {db[key].name} {db[key].pay}")
    db.close()


def update_db_classes():
    db = shelve.open(db_name)
    for key in db:
        item = db[key]
        item.give_raise(.20)
        db[key] = item
    db.close()


if __name__ == '__main__':
    make_db_classes()
    dump_db_classes()
    update_db_classes()
    dump_db_classes()
