# function in -bulid functiuon like ,len, print etc

'''print("HELLOE WORD")
print("Musharraf ")
a=len("musharraf khan")
print(a)
'''


#user defin
# def function_name
def vir(a,b):
   # a=input(print("Enter the value of a :"))
    # b=input(print("Enter the value of b :"))
    print("add is :",a+b)
    print("sub is :",a-b)
    print("mil is :",a*b)
    print("div is :",a/b)
    
vir(8,9)

def py(name):
    print("Good moring  :",name)
    
  
py("musharraf")





# types of arrgument  or functiokn arrgyumnet
#    1) Position---> order should be maintained 


def posi(firstname,lastname):
    print("HEllo mr : ",firstname,lastname)
    
posi("Musharraf ","khan")
    

#  2) keyword arrgument 
def greaat(firstname,lsatname):
     print("good morring ",firstname,lsatname)
     
greaat(lsatname="khan",firstname="sammer ")





# 3) Defalult 
def greaat(firstname="geust"):
     print("good morring ",firstname)
     
greaat()
greaat("vir")




# 4) variable length argument 
def  test(*args):
    print(args)
    print(len(args))
    print(type(args))
    
test("inda","musharrafd","kali","op")



# use keyword
def  test(**kwargs):
    print(kwargs)
    print(len(kwargs))
    print(type(kwargs))
    
test(country="indai",firstname="musharraf")