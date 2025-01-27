'''    


# single thread 
from time import sleep

class A:
    
    def run(self):
        for i in range(2):
            print("Musharraf")
            sleep(1)
            
            
class B:
    def run(self):
        for i in  range(2):
            print("khan")
            sleep(1)
t1=A()
t2=B()
t1.run()
t2.run()



'''





# multithreading
print(" multithreading..................\n..................................................................................................")
from threading import Thread
from time import sleep

class D(Thread):
    
    def run(self):
        for i in range(2):
            print("Vir")
            sleep(1)
            
            
class F(Thread):
    def run(self):
        for i in  range(2):
            print("Ajmer")
            sleep(1)
t1=D()
t2=F()
t1.start()
t2.start()

t1.join()
t2.join()

