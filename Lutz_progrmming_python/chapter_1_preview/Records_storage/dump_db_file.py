from Lutz_progrmming_python.chapter_1_preview.Records_storage.make_db_files import load_db

db = load_db()
for key in db:
    print(f'{key} =>\n\t{db[key]}')
