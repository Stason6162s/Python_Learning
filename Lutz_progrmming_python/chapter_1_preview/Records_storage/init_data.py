# Records of data base
anton = {'name': 'Anton Kobeshev', 'age': 33, 'pay': 63000, 'job': 'Techician'}
jonie = {'name': 'Evgeniy Zolotuchin', 'age': 43, 'pay': 63000, 'job': 'Techician'}
andrm = {'name': {'first': 'Mikhail', 'last': 'Andreev'},
         'age': 31,
         'job': ['PE Engineering', 'IAS'],
         'pay': (80000, 90000)}
# Data base

db = {'anton': anton, 'jonie': jonie, 'andrm': andrm}

if __name__ == '__main__':
    for key in db:
        print(f"{key} => {db[key]}")
