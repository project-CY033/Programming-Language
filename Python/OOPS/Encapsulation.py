# Encapsulation 

#                                                |--------------------------------------------|
#                                                |     Encapsulation                          |
#                                                |--------------------------------------------|
#                        |--------------------------------------------|---------------------------------------|
#                        |                                                                                    |
#                        |                                                                                    |
#  |------------------------------------------------|                                  |-------------------------------------------|
#  | single unnderscore eg--> _a=10(protected)      |                                  |Double underscore eg---> __a=20(private)   |
#  |------------------------------------------------|                                  |-------------------------------------------|



class f:
    a=input("Enter your name :")
    _b=eval(input("Enter your  age :"))
    __c=input("Enter you department: ")
    def don(self):
        print(" Your name is ",self.a)
        print("your age is ",self._b)
        print("your department is ",self.__c)
obj=f()
obj.don()
en=[]
while True:
    y=input("you want to do : ")
    if y.lower() == 'yes':
        print('conti........')
        obj.don()
        en.append(obj.a,obj._b,obj.__c)  # not access becassues c is private   
    else:
       print(en)
        