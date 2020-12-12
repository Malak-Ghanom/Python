#Write a program that adds up the sizes of all the files in the current directory,
#  and prints the result.

from os.path import getsize
from os import getcwd, listdir

dir = getcwd()
total_size = 0

for file in listdir(dir):
    print(f"File name is: {file} and the size of file is {getsize(file)}")
    total_size += getsize(file)

print(f"The total size is: {total_size}")
