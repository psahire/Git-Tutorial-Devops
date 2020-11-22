class Operations:
    def __init__(self, x, y):
        self.n1 = x
        self.n2 = y

    def sumx(self):
        return self.n1 + self.n2

    def minus(self):
        return self.n1 - self.n2

    def multiple(self):
        return self.n1 * self.n2

    def divider(self):
        return self.n1 / self.n2


op = input("Enter the Operations : ")
if op == "+":
    i = Operations(5, 4)
    x = i.sumx()
elif op == "-":
    i = Operations(5, 4)
    x = i.minus()
elif op == "*":
    i = Operations(5, 4)
    x = i.multiple()
elif op == "/":
    i = Operations(5, 4)
    x = i.divider()
else:
    print("Invalid Operator")
    
print(x)
