'''print("this is the info of student :")
def Name():
    
    name=input("Enetr uour name : ")
    L=[name]
    #print(type(L))
    print(L)
def Collegeid():
    college=input("Enter your college id :")
    tup={college}
    print(tup)
def phone():
    no=input("Department :")
    
    S={no}
    print(S)
    
obj=Name()
obj1=Collegeid()
obj2=phone()'''


 
# throught dictionare4y


class A():
  def show(self):       
    dic={"a":"","b":"","c":""}
    name=input("Enter your name :")
    age=input("Enter your  age :")
    department=input("Enter you department: ")
    dic["a"] =name
    dic["b"]=age
    dic["c"]=department
    print(dic)
obj = A()
entity=[]
while True:
    print("Do you want to add an entry?")
    choice = input("Enter 'yes' to add or any other key to exit: ")
    if choice.lower() == 'yes':
       print("OK, now we will continue...")
       entry=obj.show()
       entity.append(entry)
    else:
       print("Thanks for using this ")



'''


class A():
    def show(self):
        dic = {"Name": "", "Age": 0, "Department": ""}
        name = input("Enter your name: ")
        age = input("Enter your age: ")  # Convert age to int
        department = input("Enter your department: ")
        dic["Name"] = name
        dic["Age"] = age
        dic["Department"] = department
        return dic  # Return the dictionary

obj = A()
entity = []

while True:
    print("Do you want to add an entry?")
    choice = input("Enter 'yes' to add or any other key to exit: ")
    if choice.lower() == 'yes':
        print("OK, now we will continue...")
        entry = obj.show()  # Get the dictionary entry
        entity.append(entry)  # Append the entry to the list

    else:
        print("Thanks for using this ")
        print(entity)
        break  # Exit the loop if the user doesn't want to add more entries
'''
 