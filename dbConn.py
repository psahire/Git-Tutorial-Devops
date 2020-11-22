import pyodbc
import pandas as pd

def printtoHTML(list):
    print(list[0])

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-D63SI5E\TESTSQLSERVER;'
                      'Database=SSISPractice;'
                      'Trusted_Connection=yes')

curr = conn.cursor()

i = curr.execute('select * from test')
print(curr.fetchone())
for row in i:
    printtoHTML(row)


