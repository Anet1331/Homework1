import csv

afile = open('Books.csv', 'a')
book = input('Введите название книги: ')
author = input('Введите автора книги: ')
year = input('Введите год издания книги: ')

newline = book + "," + author + ", " + year + "\n"
afile.write(str(newline))
afile.close()

afile = open('Books.csv', 'r')
for row in afile:
    print(row)
afile.close()
