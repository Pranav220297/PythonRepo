from InvalidUserError import *
class User:
    
    def __init__(self,uname,passw,fname,lname,dob,street,city,state,country,pin):
        self.uname=uname
        self.passw=passw
        self.fname=fname
        self.lname=lname
        self.dob=dob
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.pin=pin
    def verifyUser(self,uname,passw):
        print("from User")
        if(self.uname==uname) and (self.passw==passw):
            return True
        else:
            raise (InvalidUserError("From Invalid user",uname))
    def display(self):
        print(self.fname)
        print(self.lname)
        print(self.dob)
        print(self.street)
        print(self.city)
        print(self.state)
        print(self.country)
        print(self.pin)
    
user1=User("gopi",9908,"g","k","18-09-1999","street","city","state","india",522303)
try:
    output = user1.verifyUser("abc","124")
    print(output)
except InvalidUserError as e:
    print (e.message)
    print (e.userid)
# print(user1.verifyUser("gopi",9908))
# user1.display()
# print()
# user2=User("gopi",9908,"g","k","18-09-1999","street","city","state","india",522303)
# print(user2.verifyUser("gopi",998))
# user2.display()

