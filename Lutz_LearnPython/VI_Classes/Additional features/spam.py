class Spam:
    numInstance = 0

    def __init__(self):
        Spam.numInstance += 1

    def print_NumInstance():
        print('Numbers of instance: ', Spam.numInstance)


