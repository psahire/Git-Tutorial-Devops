
'''

#Puzzle 1
n = int(input())

if n >= 1 and n <= 100:
    if n % 2 != 0:
        print("Weird")
    elif ((n % 2 ==0) and (n in list(range(2,5)))):
        print("Not Weird")
    elif ((n % 2 == 0) and (n in list(range(6,21)))):
        print("Weird")
    elif ((n % 2 == 0) and (n > 20)):
        print("Not Weird")
else:
    print("invalid number")
---------------------------------------------------------
#Puzzle 2
a = int(input())
b = int(input())
if ((a >= 1 and a.__pow__(10,10)) and (a >= 1 and a.__pow__(10,10))):
    print(a+b)
    print(a-b)
    print(a*b)

 --------------------------------------------------------
 #Puzzle 3
a = int(input())
b = int(input())

print('{0} \n{1}'.format((a//b), (a/b)))
 --------------------------------------------------------
 #Puzzle 4


n = int(input())
if n >= 1 and n <=20:
    list = list(range(n))
    for i in list:
        print(i**2)

 --------------------------------------------------------
 #Puzzle 5

import calendar
def checkLeapYear(x):
    if calendar.isleap(x):
        return True
    else:
        return False

n = int(input())
resule = checkLeapYear(n)
print(resule)
----------------------------------------------------

list = ['I','Want',4,'Apples']
listtoprint = ' '.join(map(str,list))

print(listtoprint)



print("Empty Tuple")
Tuple1 = ()
print(Tuple1)

print("Tuple with String")
Tuple1 = ("Hello","Pritam")
print(Tuple1)

print("Tuple with List")
list = [1,2,3,4]
Tuple1 = tuple(list)
print(Tuple1)

print("Tuple with built in function")
Tuple1 = tuple("Pritam")
print(Tuple1)

list = [1,3,4,5,5]
try:
    print(list[0])
    print(list[5])
except IndexError:
    print("An Error Occured")

with open('geeks.txt','r') as file:
    data = file.readlines()
    for d in data:
        word = d.split()
        print(word)


import re
with open('geeks.txt','r') as file:
    data = file.readlines()
    for i in data:
        j = re.findall('\S+@\S+',i):
        print(j)'''


sum = lambda x,y:x+y

print(sum(4,3))