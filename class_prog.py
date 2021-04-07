class User:
    def __init__(self,userid,password,firstname,lastname):        
        self.userid = userid        
        self.password = password        
        self.firstname=firstname        
        self.lastname=lastname
        self.dob = None 
        self.street =  None  
        self.City =  None  
        self.State =  None  
        self.Country =  None  
        self.pin = 0 

    

    def verifyUser(self, userid, password):        
        if (userid == self.userid and password == self.password):
            return True
        else:
            return False   
    

user1 = User("abcd", "12345","pranav", "kumar")
user1.dob = "12th April 1997"
user1.street ="Hanuman Mandir"
user1.City = "Dhanbad"
user1.State ="Jharkahand"
user1.Country = "India"
user1.pin = 828105

output = user1.verifyUser("abc","124")
print(output)