from classEmployee import Employee

class teacher(Employee):
    __numberhour = 0

    def __init__(self,id,name,phone,state,startdate,numberhour):
        Employee.__init__(self,id,name,phone,state,startdate)
