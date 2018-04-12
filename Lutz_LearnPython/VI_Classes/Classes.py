class C2:
    pass


class C3:
    pass


class C1(C2, C3):
    def setname(self, who):
        self.name = who


# I1 = C1()
# I2 = C1()

I1, I2 = C1(), C1()
I1.setname('bob')
I2.setname('mel')

classList = [I1, I2]

for clasS in classList:
    print(clasS.name)


class C4:
    def __init__(self, who):
        self.name = who


I3 = C4('bib')
print(I3.name)
