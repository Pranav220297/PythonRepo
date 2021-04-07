class Patient:
    def __init__(self,patientid,password,firstname,lastname):        
        self.patientid=patientid
        self.password = password        
        self.firstname=firstname        
        self.lastname=lastname
        self.dob = None 
        self.street =  None  
        self.City =  None  
        self.State =  None  
        self.Country =  None  
        self.pin = 0 

class Doctor:
    def __init__(self,doctorid, firstname,lastname,specification):
        self.doctorid=doctorid
        self.firstname=firstname
        self.lastname=lastname
        self.specification=specification
        self.affihospital= None

class Appointment:
    def __init__(self,appid,patientid,apptime,appdate):
        self.appid=appid
        self.patientid=patientid
        self.apptime=apptime
        self.appdate=appdate
        self.status=status 

class Prescription:
    def __init__(self,docid,patientid, medicine, observation):
        self.docid=docid
        self.patientid=patientid
        self.medicine= medicine
        self.observation=observation

class Review:
    def __init__(self,patientid, review):
        self.patientid=patientid
        self.review=review
