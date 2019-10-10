"""
Storage db form operating memory to a text file
"""
db_file_name = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'


def store_db(db, dbfilename=db_file_name):
    """
    It saves the database in a text file
    :param db: path or name of data base
    :param dbfilename: name of data base file
    :return:None
    """
    db_file = open(dbfilename, 'w')
    for key in db:
        print(key, file=db_file)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=db_file)
        print(ENDREC, file=db_file)
    print(ENDDB, file=db_file)
    db_file.close()


def load_db(dbfilename=db_file_name):
    """
    It restores data by reconstructing the database
    :param dbfilename:Path or name of database
    :return:None
    """
    db_file = open(dbfilename)
    print(f'open the {dbfilename}')
    import sys
    sys.stdin = db_file
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from init_data import db

    store_db(db)
