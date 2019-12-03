# Formatting strings
name = 'Star'
age = 32
f_string = f"My name is {name}, i am {age} years"
print(f_string)
place_holders_string = 'My name is %s, i am %d years' % (name, age)
print(place_holders_string)
format_string = "My name is {0}, i am {1} years".format(name, age)
print(format_string)


# Documentation of code

def some_function(any_type, string='', integer=0):
    """
    The function print string from own arguments
    :param any_type: the argument may be any type
    :param string: the argument should be string, and default value - empty string
    :param integer: the argument should be string, and default value - zero
    :return: Arguments string
    """
    return_string = f"My name is {any_type}, i am {str(integer)} {string}"
    return return_string


# Next...
if __name__ == '__main__':
    print(some_function('Stars', 'years', 32))
