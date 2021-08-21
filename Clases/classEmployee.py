from Clases.classPerson import Person

class Employee(Person):
    __stardate = ""

    def __init__(self, id, name, last_name, phone, mobile_phone, age, state, stardate):
        Person.__init__(self, id, name, last_name, phone, mobile_phone, age, state)
        self.__stardate = stardate

    def gestartdate(self):
        return self.__stardate

    def setstardate(self,stardate):
        self.__stardate = stardate