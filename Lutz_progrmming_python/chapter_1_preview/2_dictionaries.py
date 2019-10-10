"""
How to create and use a dictionaries
"""
anton = {'name': 'Anton Kobeshev', 'age': 33, 'pay': 63000, 'job': 'Techician'}
jonie = {'name': 'Evgeniy Zolotuchin', 'age': 43, 'pay': 63000, 'job': 'Techician'}
print(f"{anton['name']} {jonie['job']}")

rim = dict(name='Roman Ischakov', age=32, pay=120000, job='Maintenance manager')
print(f"{rim['name']} - {rim}")

sur = {}
sur['name'] = 'Artem Surkov'
sur['age'] = 35
sur['pay'] = 135000
sur['job'] = 'Manager of engineering'
print(f"{sur['name']} - {sur}")

# Combining two lists
fields = ['name', 'age', 'pay', 'job']
values = ['Stanislav Alekseev', 33, 96700, 'Sr. IAS']
print(list(zip(fields, values)))
stason = dict(list(zip(fields, values)))
print(stason)

# Empty dictionary from list
records = dict.fromkeys(fields, '?')
print(records)

colleagues = [stason, rim, sur, anton, jonie]

for person in colleagues:
    print(person['name'], person['job'], sep=' - ')

names = [person['name'] for person in colleagues]
print(names)
jobs = list(map((lambda x: x['job']), colleagues))
print(jobs)

# SQL like query
most_pays = [rec['name'] for rec in colleagues if rec['pay'] >= 100000]
print(most_pays)
