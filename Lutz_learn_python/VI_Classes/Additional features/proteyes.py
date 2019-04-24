class Classic:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError


x = Classic()
print(x.age)


#  print(x.name)  # Raise exception AttributeError


class NewProps:
    def get_age(self):
        return 'get_age: 40'

    age = property(get_age, None, None, None)


y = NewProps()
print(y.age)
