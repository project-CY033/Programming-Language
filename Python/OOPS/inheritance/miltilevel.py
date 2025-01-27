class Father():
    surname="khan"
class Son(Father):
    def kaal(self):
        print("Musharraf",self.surname)
class Gson(Son):
    def hack(self):
        print("Nafis",self.surname)
class fson(Gson):
    def kali(self):
        print("Ali",self.surname)
        
d=Son()
d.kaal()

fg=Gson()
fg.hack()

kh=fson()
kh.kali()



