from User import *
class Doct(User):

    def __init__(self,unam,passw,fname,lname,dob,street,city,state,country,pin,spec):
        super().__init__(unam,passw,fname,lname,dob,street,city,state,country,pin)
        self.spec=spec
    def verifyUser(self,uname,passw):
        print(" from doctor ")
        if(self.uname==uname) and (self.passw==passw):
            return True
        else:
            return False
    
d1=Doct("gopi",9908,"g","k","18-09-1999","street","city","state","india",522303,'dental')
print(d1.uname)
d1.verifyUser("gopi",9908)
u1=User("gopi",9908,"g","k","18-09-1999","street","city","state","india",522303)
u1.verifyUser("gopi",990)

u1=d1
u1.verifyUser("rr",990)

u1=d1
u1.verifyUser("wd",9)



