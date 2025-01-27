print("Inheritance :")

class Father():
    def lands(self):
        print("HAving 50 Ekar lands")
class Son(Father):
    def Money(self):
        print( "Having 100 core in his account ")
S=Son()      # Son classs can be access both father and itd own class
S.lands()
S.Money() 
'''
F=Father()        # but fathe can't inherit its child class 
F.lands()
F.Money()'''



# Singleinheritance 
print("Single-inheritance \n..............................................")

class A():
    n1=90
    n2=80
   
    def add(self):
        print("Addition is :",self.n1+self.n2)
    def sub(self):
        print("Subtraction is :",self.n1-self.n2)
        
# Single inheritance \
    
class B(A):
    def mil(self):
        print("miltiplication is :",self.n1*self.n2)
    def div(self):
        print("Division is :",self.n1/self.n2)
        
    def reminder(self):
        print("riminder is :",self.n1%self.n2)

    
    
print("Output of class A \nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")    
obj=A()  # we can only access add, sub only 
obj.add()
obj.sub()
    
     
print("Output of class B \n**********************************")
# calling class B
obj=B()              # we can access all the function throught class " B "
obj.add()
obj.sub()
obj.mil()
obj.div()
obj.reminder()



# multilevel inheritance
print("multilevel inheritance \n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

class Fath:
    a = 10
    b = 20  

class Son(Fath):
    def addition(self):
        print("Addition is", self.a + self.b)

    def subtraction(self):
        print("Subtraction is", self.a - self.b)

class Sson(Son):
    def multiplication(self):
        print("Multiplication is", self.a * self.b)

obj = Sson()
obj.addition()
obj.subtraction()
obj.multiplication()



