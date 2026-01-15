# Open the book
my_open_book = open('CatInTheHat.txt')

# Print every line in the book
the_line = my_open_book.readline()
while the_line != '':
    print(the_line, end='')
    the_line = my_open_book.readline()

print("The End.")
