#Write a program that reads the contents of sentences.txt 
# and writes exactly the same contents to the file sentences.tmp. 
# Then open the file sentences.tmp and display the contents.


file1 = open("D:\\python\\CA12\\sentence.txt")

file2 = open("sentence.tmp","w")

for line in file1:
    file2.write(line)
file2.close()

with open('sentence.tmp') as fp:
    buffer = fp.read()

print(buffer)