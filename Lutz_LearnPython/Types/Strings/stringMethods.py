import sys

# REPLACE
print('spammy'.replace('mm', 'xx'))  # simple replace
print('a$sdf$$redefe$'.replace('$', 'STAS'))  # find and replace all concurrence
print('a$sdf$$redefe$'.replace('$', 'STAS', 1))  # find and replace specified concurrence
# transform to list and back to string
S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'z'
S = "".join(L)
print(S)
# JOIN example
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
# Splicing a string
line = 'aaa bbb ccc'
col1 = line[:3]
col2 = line[4:7]
col3 = line[8:]
print(col1, ' ', col2, " ", col3)
print(line.split())
line2 = 'bob,hacker,40'
print(line2.split(','))
line3 = "The Knight who say Ni!\n"
# other methods
print(line3)
print(line3.upper())
print(line3.isalpha())
print(line3.endswith('Ni!\n'))
print(line3.startswith('The'))
print(help(S.startswith))
# Format expression
print('The knight who say %s' % 'Ni!')
print('%d %s %d you' % (1, 'spam', 4))
print('%s---%s---%s' % (42, 1.23, [1, 2, 3]))
print("%(n)d for %(x)s" % {'n': 1, 'x': 'you'})
reply = """
Hello %(name)s!
Happy %(age)d years!!!
"""
value = {'name': 'Stas', 'age': 31}
print(reply % value)
name = 'Olga'
age = 26
values = vars()
print(reply % values)
# Format method
template = '{0}, {1} and {2} with position args'  # position args
print(template.format('spam', 'ham', 'eggs'))  # naming args
template = '{motto}, {pork} and {food} with naming args'
print(template.format(motto='spam', pork='ham', food='eggs'))
template = '{motto}, {0} and {food} with common args'
print(template.format('ham', motto='spam', food='eggs'))  # together variant
print('####')
print('my {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
print('my {config[spam]:>10} runs {sys.platform}'.format(sys=sys, config={'spam': 'laptop'}))
somelist = list('SPAM')
print('first = {0[0]} third = {0[2]}'.format(somelist))
print('first = {0} last = {1}'.format(somelist[0], somelist[-1]))
parts = somelist[0], somelist[-1], somelist[1:3]
print('first = {0}, last = {1} and slice {2}'.format(*parts))
