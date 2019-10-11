"""
Pickle module learning
"""
import pickle

from Lutz_progrmming_python.chapter_1_preview.Records_storage.init_data import db


def make_db_pickle(database):
    with open('people-pickle', 'wb')as file:
        pickle.dump(database, file)


def dump_db_pickle():
    with open('people-pickle', 'rb') as df_file:
        db_file = pickle.load(df_file)
    for key in db_file:
        print(f'{key} => \n\t {db_file[key]}')
    return db_file


def update_db_pickle():
    with open('people-pickle', 'rb') as db_file:
        database = pickle.load(db_file)
    database['anton']['name'] = 'Anton Kobeshev'
    with open('people-pickle', 'wb') as db_file:
        pickle.dump(database, db_file)


def make_db_pickle_recs():
    for key in db:
        with open(key + '.pkl', 'wb') as rec_file:
            pickle.dump(db[key], rec_file)


def dump_db_pickle_recs():
    import glob
    for file_name in glob.glob('*.pkl'):
        with open(file_name, 'rb') as rec_file:
            record = pickle.load(rec_file)
            print(f'In the {file_name} containe: \n\t {record}')


def update_db_pickle_recs(rec_name):
    with open(rec_name + '.pkl', 'rb') as rec_file:
        record = pickle.load(rec_file)
    record['name'] = 'Anton Kobeshev'
    with open(rec_name + '.pkl', 'wb') as rec_file:
        pickle.dump(record, rec_file)


if __name__ == '__main__':
    # make_db_pickle(db)
    # update_db_pickle()
    # dump_db_pickle()
    make_db_pickle_recs()
    dump_db_pickle_recs()
    update_db_pickle_recs('anton')
    dump_db_pickle_recs()
