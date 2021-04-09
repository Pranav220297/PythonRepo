    
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, empid, empname,basic, hra):
        self.id = empid
        self.name = empname
        self.basic = basic
        self.hra = hra
    @abstractmethod
    def calcSal(self):
        pass
class Developer(Employee):
    def __init__(self, empid, empname,basic, hra,skillall):
        super().__init__(empid, empname,basic, hra)
        self.skillall = skillall
    def calcSal(self):
        return self.basic+self.hra+self.skillall
class Manager(Employee):
    def __init__(self, empid, empname,basic, hra,bonus):
        super().__init__(empid, empname,basic, hra)
        self.bonus = bonus
    def calcSal(self):
        return self.basic+self.hra+self.bonus
class TechLead(Employee):
    def __init__(self, empid, empname,basic, hra):
        super().__init__(empid, empname,basic, hra)
    def calcSal(self):
        return self.basic+self.hra
emp = Developer(5000,"Gnaehs", 2222,222,1000)
print(emp.calcSal())
emp1 = Manager(5000,"Gnaehs", 2222,222,100)
print(emp1.calcSal())
emp2=TechLead(5001,"gopi",2222,222)
print(emp2.calcSal())