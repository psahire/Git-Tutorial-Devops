import pyodbc
import pandas as pd

conn = pyodbc.connect(r'Driver={SQL Server};'
                      r'Server=DESKTOP-D63SI5E\TESTSQLSERVER;'
                      r'Database=SSISPractice;'
                      r'Trusted_Connection=yes;')

curr = conn.cursor()
curr.execute('select *  from customers')

data1 =     

curr.execute('''INSERT INTO [dbo].[customers]
         ([customerid]
         ,[fname]
        ,[lname])
    VALUES
           (3,'Imran','Khan'),
           (4,'Jigar','Patel')
           ''')
#conn.commit()'''
#with open('data.txt','w') as file:
for row in curr:
   print(str(row))
 #       file.writelines(str(row))
#file.close()

#SQL Pandas
#sql_query = pd.read_sql_query('select * from test',conn)
#print(sql_query)
#print(type(sql_query))