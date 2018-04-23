def fetch(obj, index):
    try:
        return obj[index]
    except IndexError:
        print('Got Exception')



x = 'Spam'
print(fetch(x, 3))
print(fetch(x, 4))
