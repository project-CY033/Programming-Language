'''import hierarchical

hierarchical.Son1



import demo
demo.show

'''


from abc import ABC,abstractmethod
class Car(ABC):
    def Show(self):
        print("Every car have a 4 wheel")
    @abstractmethod
    def Speed(self):
        pass
class Maruti(Car):
    def Speed(self):
        print("Speed is 108km/hr")
class Suziki(Car):
    def Speed(self):
        print("speed is 70km/h")

obj=Maruti()
obj.Show()
obj.Speed()

obj2=Suziki()
obj2.Show()
obj2.Speed()    