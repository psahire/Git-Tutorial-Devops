"""prices = [10,20,30]
total = 0
for i in prices:
    total += i
print(f"Total :  {i}")

for i in range(0,2):
    for j in range(0,3):
        print(f'({i} , {j})')

list = [5,2,5,2,2]
for i in list:
    output = ''
    for j in range(i):
        output += 'X'
    print(output)

## Find largest number in list

list = [1,2,13,4,5]
max = 0
for i in list:
    if i > max:
        max = i
print(max)

str = "Hello this is Pritam"
x = ('Pritams' in str)
if x:
    print("Found")
else:
    print("Not Found")
print(str.replace('this','these'))
print(4 ** 3)
str = input("Number :")
x = 5
print(int(str) + x)
price = 25
print(price > 10 and price < 20)

weight = int(input("Weight : "))
n = input("(K)g or (L)b : ").upper()
if n == "K":
    result = weight / 0.45
elif n == "L":
    result = weight * 1.6
else:
    print("Invalid Unit")
    quit()
print(f"Total Weight: {result}")

i = [1,2,3,4,5]
x = range(0,10)
for j in x:
    i.append(j)
print(i)
print(i.count(10))

s_tuple = (3,4,5)
print(s_tuple[0])
s_tuple[2] = 10
print(s_tuple)

filename = "c:\sample.txt"
fileext = filename[filename.find(".") + 1:]
print(f"File Extension is : {fileext}")

filename = open("test.txt","r")
print(filename.readlines()[1])
filename.close()"""

from Student import Student
Student1 = Student("Ganesh",8.3)
print(Student1.gpa)