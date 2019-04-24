title = "Stas" ' the ' "best " 'programer'
print(title)
title = "Stas", ' the ', "best ", 'programer'
print(title)
s = 'a\nb\tc\\a'
print(s)
print('####')
#  open for writing in file
writeFile = open(r"C:\MCS\Config.dat", 'w')
# S = "Test file"
# writeFile.write(S)
#  open for reading from file
readFile = open(r"C:\MCS\Config.dat", 'r')
# text = readFile.readline()
# print(text)

#  block strings
mantra = """Always look
on the bright
side of life
"""
writeFile.write(mantra)
text = readFile.readlines()

print(text)
#  Iterable of string
myJob = 'hacker'
for c in myJob:
    print(c, end=" ")
print("k" in myJob)
print('z' in myJob)

#  Index of Strings
S = 'SliceOfSpam'
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

#  The third limit
S1 = '12345678910'
print(S1[::2])
print(S1[::-1])

#  Converting strings
S2 = "42"
I = 1
#  S2 + I return Errors, need to trasform type
print(int(S2) + I)
print(S2 + str(I))

# Convert to ASCII
print(ord('s'))
print(chr(115))

S3 = 'That is %d %s bird' % (1, 'dead')  # format expression

S4 = 'That is {0} {1} bird '.format(1, 'dead')  # format method

print(S3, ' ', S4)
