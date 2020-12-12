#Write a program that reads the lines from flatland.txt and
#displays only those lines that contain the word 
#Triangles, Squares, Pentagons, Hexagons. Ignore the cases of the words.

my_file = open ('D:\\python\\CA12\\flatland.txt','r')
keyword = ['Triangles', 'Squares', 'Pentagons', 'Hexagons']

for line in my_file:
    for key in keyword:
        if key in line:
            print(line)
            break
my_file.close()