#Modify the code in csv_file_io.py to do the following:
# Write more lines into the file based on user input.
# Add a Genre column into the CSV file an populate the list with the movie genres.

from csv import writer,reader

# Reading and Writing CSV Files
# > Open the CSV file for writing
fp = open("movies.csv", "w")

# > Create a CSV writer
csv_writer = writer(fp)
csv_writer.writerow(["ID" , "Movie", "Rating","genre"])
ID = 0
add = 'Y'

while add != "N":
    movie = input('insert the movie name: ')
    rate = int(input("insert the movie rate: "))
    genre = input('insert the genre: ')
    csv_writer.writerow([ID,movie,rate,genre])
    ID += 1
    add = input('Do you want to add another row? Y/N :').upper()

fp.close()

fp = open("movies.csv")
csv_reader = reader(fp)
for row in csv_reader:
    print(f"Movie #{row[0]} - '{row[1]}' has a rating of {row[2]} and a genre of {row[3]}.")

# > Close the file
fp.close()
