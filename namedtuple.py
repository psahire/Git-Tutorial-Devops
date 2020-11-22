class Person:
       def __init__(self,n,p,i):
              self.pnamename = n
              self.personality = p
              self.issitting = i

       def sitdown(self):
              self.issitting == True
       def situp(self):
              self.issitting == False

class Robot:
       def __init__(self,name,color,weight):
              self.name = name
              self.color = color
              self.weight = weight
       def introself(self):
              print("My name is " + self.name)
r1 = Robot("Pritam","Blue",24)
#r1.introself()

p1 = Person("xxx","Romantic",True)
p1.robotowned = r1
p1.robotowned.introself()