# Polymorphims

#                                                |--------------------------------------------|
#                                                |    Polymorphims                            |
#                                                |--------------------------------------------|
#                        |--------------------------------------------|---------------------------------------|
#                        |                                                                                    |
#                        |                                                                                    |
#  |------------------------------------------------|                                  |-------------------------------------------|
#  |          overloading  method                   |                                  |         overriding   method               |
#  |------------------------------------------------|                                  |-------------------------------------------|



print(len("Musharraf khan"))         # find  length by character wise 
print(len(("Nafis","Musharraf")))    # find  length by string  wise



# method overloading 
class A:
    def show(self):
        print("Welcome........")
        
    def show(self,firstname):
        print("Welcome",firstname)
        
    def show(self,firstname='', lastname=''):
        print("welcome",firstname,lastname)
obj=A()
obj.show()
obj.show('Musharraf')
obj.show('Musharraf','khan')



# or we can also write this program like this 
class B:
     def show(self,firstname='', lastname=''):
        print("welcome",firstname,lastname)
o=B()
o.show()
o.show("nafis")
o.show('Nafis','khan')
