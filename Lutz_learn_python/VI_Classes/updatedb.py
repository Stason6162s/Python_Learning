import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '\t= ', db[key])
stas = db['Stas Alekseev']
print(stas)
stas.give_raise(.05)
print(stas.__class__)
db['Stas Alekseev'] = stas
db.close()
