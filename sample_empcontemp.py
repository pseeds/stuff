# -*- coding: utf-8 -*-

class Staffing_Model(object):
     
    def __init__(self, first, last, rate, vacation):
      self.first_name = first
      self.last_name = last
      self.pay_rate = rate
      self.vacation_days = vacation

    def get_name(self):
      fl_name = ""
      fl_name += self.last_name
      fl_name += ','
      fl_name += self.first_name
       
      if (type(self).__name__ == "Employee"):
        fl_name += " [E]"
      elif (type(self).__name__ == "Contractor"):
        fl_name += " [C]"
      elif (type(self).__name__ == "Temporary"):
        fl_name += " [T]"
      else:
        fl_name += "[ERROR]"
        
      return fl_name
        
    def get_pay_rate(self):
      return self.pay_rate
        
    def get_vacation_days(self):
      return self.vacation_days
        

class Employee(Staffing_Model):

    def __init__(self, first, last, rate, vacation):
      # call parent constructor to set first, last, rate, vacation
      super(Employee, self).__init__(first, last, rate, vacation)


    def get_agency(self):
      return self.agency_name


class Contractor(Staffing_Model):

     def __init__(self, first, last, rate, agency, vacation):
        
       if vacation > 0:
          vacation = 0 
       # call parent constructor to set first, last, rate, vacation
       super(Contractor, self).__init__(first, last, rate, vacation)   
       self.agency_name = agency


     def get_agency(self):
       return self.agency_name


class Temporary(Staffing_Model):

    def __init__(self, first, last, rate, agency, vacation):
        
      if vacation > 0:
         vacation = 0 
      # call parent constructor to set first, last, rate, vacation
      super(Temporary, self).__init__(first, last, rate, vacation)   
      self.agency_name = agency

 
    def get_agency(self):
      return self.agency_name


emp = Employee("Paul", "Seeds", 65.00, 28)
print(emp.get_name())
print(emp.get_pay_rate())
print(emp.get_vacation_days())

cont = Contractor("Paul", "Seeds", 70.00, "Funco", 10)
print(cont.get_name())
print(cont.get_pay_rate())
print(cont.get_vacation_days())
print(cont.get_agency())

tempr = Temporary("Paul", "Seeds", 75.00, "NoFunco", 15)
print(tempr.get_name())
print(tempr.get_pay_rate())
print(tempr.get_vacation_days())
print(tempr.get_agency())
