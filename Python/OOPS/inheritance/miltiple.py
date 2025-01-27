class kabadi():
    km="total member is 90  at present "
    def show(self):
        print("Team kabadi sucessfuly register now .........",self.kabadi)
    def cr(self):
        print("crikat tem registered now.....",self.cr)
    def bass(self):
        print("baskit team register now........",self.bass)
        
class don():
    staf=10
    def staf_km(self):
        print("staf member is ",self.staf)
    def st_cr(self):
        print("toral member of cr is ",self.staf)


class team(kabadi,don):
    print("tema sucessfuly created ................")
    
d=team()
d.show()
d.cr()
d.bass()
d.staf_km()
d.st_cr()