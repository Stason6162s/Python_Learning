import sys

template = "%s%s %s"
print(template % ('T326', '062839', '201712290240'))

series = 'T326'
chassis = '062839'
sequence = '201712290240'
values = vars()  # create dictionary from all variable in codes

template = '%(series)s%(chassis)s -- %(sequence)s'
print(template % values)

X = 'My %(type)s runs on %(platform)s' % {'type': 'laptop', 'platform': sys.platform}
Y = 'My %(type)s runs on %(platform)s' % dict(type='notebook', platform=sys.platform)
print(X, Y)

somelist = list("Stas")
patrs = somelist[0], somelist[-1], somelist[1:3]

print('first = %s, last = %s and slice = %s' % patrs)
