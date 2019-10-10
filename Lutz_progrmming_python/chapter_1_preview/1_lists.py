"""
How to create and use lists
"""

# Lists
pawka = ['Pawel Koznow', '29', 76000, 'Technicians leader']
miwka = ['Michail Spasenko', '29', 91000, 'Technicians engineer']

employees = [pawka, miwka]

for item in employees:
    print(item[0].split()[-1])
    item[2] *= 1.20

for person in employees:
    print(person[2])

# list generator
pays = [person[2] for person in employees]
print(pays)

# or map function
pays = map((lambda x: x[2]), employees)
print(list(pays))
