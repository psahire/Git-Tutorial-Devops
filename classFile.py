#test
class Employee:
    def __init__(self):
        self.salary = 1000
        self.company = 'Google'

    def empSalary(self):

        #pass
        print(f"Hello..Welcome to {self.company} salary is {self.salary}")

    @staticmethod
    def greet():
        print("Welcome to My company")

harry = Employee()
#harry.salary = 10000
harry.empSalary() #or Employee.empSalary    (harry)

harry.greet()
