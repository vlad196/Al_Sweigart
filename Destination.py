#! python3

import os

print(os.path.join('lol', 'xd', 'kek'))

print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())
os.chdir('C:\\Users\\vlad1\\PycharmProjects\\Al_Sweigart')


print(os.path.abspath('.'))
print(os.path.abspath('.\\passmanager'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))


print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Users\\vlad1', 'C:\\Windows\\System32'))

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

print(os.path.split(path))

print(path.split(os.path.sep))

print(os.path.getsize(path))
print(os.listdir('C:\\Windows\\System32\\'))