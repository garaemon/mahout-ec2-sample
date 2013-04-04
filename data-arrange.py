#! /usr/bin/python
 
import sys
import csv
import collections
 
def main(argv):
  idx = create_book_id_index()
  ratings = csv.reader(open('BX-Book-Ratings.csv', 'rb'), delimiter=';', quotechar="\"")
  out = open('Ratings.csv', 'w')
  for row in ratings:
    try:
      out.write('%s,%d,%s\n' % (row[0], idx[row[1]], row[2]))
    except KeyError:
      pass
  out.close()
 
def create_book_id_index():
  books = csv.reader(open('BX-Books.csv', 'rb'), delimiter=';', quotechar="\"")
  book_index = open('Book-ID-Index.csv', 'w')
  idx = {}
  counter = -1
  for row in books:
    counter += 1
    if counter == 0:
      continue
    book_index.write('%d,%s\n' % (counter, row[0]))
    idx[row[0]] = counter
  book_index.close()
  return idx
 
if __name__ == '__main__':
  main(sys.argv)
  
