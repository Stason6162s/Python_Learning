import shelve

from VI_Classes.person import Person, Manager

stas = Person('Stas Alekseev', 'PLC', 84000)
pasha = Person('Pavel Koznov', 'Master', 77000)
suric = Manager("Artem Surkov", 150000)
griga = Manager("Grigoriy Belyaev", 150000)

db = shelve.open('persondb')
for rec in (stas, pasha, suric, griga):
    db[rec.name] = rec
db.close()
