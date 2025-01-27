                        # Constructor 
                        # If we cannot creat a constructor the python itself creat an empty constructor 
                        # the defferenced is that we cancont pass value in it 
class g:
    age=20
    user_name="Kali"
    def __init__(self):
        name="Musharraf khan"
       # a=eval(input("Enter the value of a :"))
       #b=eval(input("Enetr the value  of b: "))
        print(name," ",self.age," ",self.user_name)
        
obj=g()


# 1>----> Default constructor
  # default constructor is also called as empty coanstructor because it dos't have paremeter 
  # self helf to access class memnber in function
print(" default constructor \n .................")
class r:
    n="vir"
    def __init__(self):           # n can be access by " self.n "  due to  " n " is not local variable of this function 
       add="Ajmer Rajasthan"      # " add "  is a local variable so it can be access with self 
       print(self.n," ", add )
    def show(self):                # it can't be call automaticall so  we need to call them " obj.show() "
        print("hello every one ehat is ")
       
obj=r()        
obj.show()





# paramertrized construcvtor----> it acept arrgument along with self 

print("Parametrized constructor \n ...................")
class p:
    name1="java"                       # name1 can be access every where in this class 
    def __init__(self,na,adderse,age):
        adderse="somalpure"
        print(age,adderse,na,self.name1)
    def sh(self):
        print(self.name1)
        
obj=p("Musharraf","somalpur",20)
obj.sh()      
        


