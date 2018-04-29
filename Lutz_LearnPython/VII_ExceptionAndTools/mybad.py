class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bridge side of life...'


try:
    raise MyBad('Stas')
except MyBad as X:
    print(X, X.args)


class BadBad(Exception):
    pass


try:
    raise BadBad('Sorry - my mistake')
except BadBad as X:
    print(X)


raise BadBad('Aagain')