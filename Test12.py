import camelot
import os


tables = camelot.read_pdf('1403004400_2020-09-09.pdf', flavor='stream')
print(tables.n)
print(tables[0].df)
tables.export('foo1.csv', f='csv')