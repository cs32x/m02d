# Open the book
my_open_book = open('CatInTheHat.txt')

# Do the indented work until all the lines have been read
    the_line = my_open_book.readline()
    print(the_line, end='')

    if the_line == '':
        break

print("The End.")
