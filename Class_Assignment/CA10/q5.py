# Write a function ext_sort(filelist) which sorts and returns a list of filenames based on their extensions.
# Input: filelist = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'] and call ext_sort(filelist)
# Return: ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']

import os

def ext_sort(sorted_filelist):   
    sorted_filelist.sort(key=lambda file:file[file.index('.') + 1])
    return sorted_filelist

filelist = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print (ext_sort(filelist))