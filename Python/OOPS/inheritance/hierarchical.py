# Hierarchical inheritance


class Musharraf():
    # properties 
    sur_name="khan"
    def show(self):
        print("My surname is ",self.sur_name)
class Son1(Musharraf):
    def power(self):
        print("This is S ",self.sur_name)
class Son2(Musharraf):
    def gk(self):
        print("This is w ",self.sur_name)
class Son3(Musharraf):
    def jk(self):
        print("this  is d ",self.sur_name)
#obj=Musharraf()        
s1=Son1()
s2=Son2()
s3=Son3()
s1.power()
s2.gk()
s3.jk()

s1.show()
s3.show()
s2.show()