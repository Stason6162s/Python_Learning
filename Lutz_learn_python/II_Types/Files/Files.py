import pickle

print('\n\t Methods for work with files')
myFile = open('myFile.txt', 'w')
myFile.write('Hello text file\n')
myFile.write('Goodbye text file\n')
myFile.close()

myFile = open('myFile.txt')
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())
print(open('myFile.txt').read())  # output all files content
for line in open('myFile.txt'):
    print(line, end=' ')
print('\n\t Writing other object in file')
X, Y, Z = 42, 44, 45
S = 'spam'
D = dict(a=2, b=3)
L = [1, 2, 3]
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
print(open('datafile.txt').read())
F = open('datafile.txt')
line = F.readline()
print(line.rstrip())
line = F.readline()
print(line)
parts = line.split(',')
numbers = [int(P) for P in parts]
print(numbers)
line = F.readline()
print(line)
parts = line.split('$')
objects = [eval(P) for P in parts]
print(objects)
print('\n\t Pickle module')
F = open('data.pkl', 'wb')
pickle.dump(D, F)
F.close()
F = open('data.pkl', 'rb')
E = pickle.load(F)
print(E)
print(open('data.pkl', 'rb').read())
