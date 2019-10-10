import pprint

mike_andreev = {'name': {'first': 'Mikhail', 'last': 'Andreev'},
                'age': 31,
                'job': ['PE Engineering', 'IAS'],
                'pay': (80000, 90000)}
print(mike_andreev['name'])
print(mike_andreev['name']['last'])
print(mike_andreev['pay'][1])

# Dictionary of dictionaries

anton = {'name': 'Anton Kobeshev', 'age': 33, 'pay': 63000, 'job': 'Techician'}
jonie = {'name': 'Evgeniy Zolotuchin', 'age': 43, 'pay': 63000, 'job': 'Techician'}

db = {}
db['anton'] = anton
db['jonie'] = jonie
print(db['anton']['name'])
print(db)
pprint.pprint(db)

for key in db:
    print(f'{key} => {db[key]["name"]}')
for record in db.values():
    print(record['name'])
print(list(db.keys()))
