# access modifire------> Are used to set the limit of  member accessibilities 
class A:   # preant class 
    a=10   # public
    _b=20  # Protected
    __c=None  #privite
    # we can access in class
    print(a," ",_b," ",__c)
    def show(self):
          self.__c=self.a+self._b
          print("Addition is ",self.__c)
obj=A()
obj.show()
print(obj._b)
# print(obj.__c)    we can't access this outside form class due ot it is privite class 


print("That is result of b class ")
class B(A):      # child 
    def vir(self):
        print(self.a)
        print(self._b)
        print(self.__c)     # this is not access because it is privite 
obj=B()
obj.show()


print("Class C :-\n......................................")
class C(A):
    pass
obj=C()
print(obj.a)
print(obj._b)
print(obj.__c)     # this is not access because it is privite 

