#Write a program to check if a given path exists in the current working directory.
#If it is found, then print the details of the path.
#Type (directory / file).
#Size in kilobytes, or megabytes.
#Creation time / access time / modification time.

from os.path import exists
from os.path import isdir, isfile
from os.path import getsize
from os import getcwd
from datetime import time
import os.path, time

file_name = 'q1.py'

if exists(file_name):
    print('found')

if isdir(file_name):
    print(f"{file_name} is a directory, with a size of {getsize(file_name)}")
    print('Creation in: %s'%time.ctime(os.path.getctime(file_name)))
    print('Accessed in: %s'%time.ctime(os.path.getmtime(file_name)))
    print('Modification in: %s'%time.ctime(os.path.getatime(file_name)))

else:
    print(f'{file_name} is a file')
    print(f"{file_name} is a directory, with a size of {getsize(file_name)}")
    print('Creation in: %s'%time.ctime(os.path.getctime(file_name)))
    print('Accessed in: %s'%time.ctime(os.path.getmtime(file_name)))
    print('Modification in: %s'%time.ctime(os.path.getatime(file_name)))