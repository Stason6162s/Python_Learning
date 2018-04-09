# unpaking arguments from collections

def func(a, b, c, d):
    print(a, b, c, d)


args = (1, 2)
args += (3, 4)
func(*args)  # unpacking list

dict_args = dict(a=1, b=2, c=3, d=4)
func(**dict_args)  # unpacking dictionary


# Only name called
def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, 3, 4, c=72)
kwonly(a=1, c=3)
kwonly(1, 2, c=66)
