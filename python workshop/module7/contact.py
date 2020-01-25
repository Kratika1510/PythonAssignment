class contact:
    def __init__(self,name,phno,em):
        self.name=name
        self.phno=phno
        self.em=em
    def set_name(self,name):
        self.name=name
    def set_phno(self,phno):
        self.phno=phno
    def set_em(self,em):
        self.em=em
    def get_name(self,name):
        return self.name
    def get_ph(self,phno):
        return self.phno
    def get_email(self,em):
        return self.em
    def __str__(self):
        return self.name+" "+self.phno+" "+self.em
def main():   
 c=contact("Kratika",'9826044',"kk@gmail.com")
 c.set_name("Kratika")    
 c.set_phno('9826044')            
 c.set_em("kk@gmail.com")
 print(c.__str__())            
main()
