class Person:#Clase
    __id = ""
    __name= ""
    __last_name=""
    __phone=""
    __mobile_phone=""
    __age = ""
    __state =""

    #contructor
    def __init__(self,id,name,last_name,phone,mobile_phone,age, state):
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__phone = phone
        self.__mobile_phone = mobile_phone
        self.__age = age
        self.__state = state

    def getID(self):
        return self.__id

    def setID(self,id):
        self.__id = id

    def getfull_name(self):
        return f"{self.__name},{self.__last_name}"

    def setfull_name(self,name,last_name):
        self.__name = name
        self.__last_name = last_name

    def getphone(self):
        return self.__phone

    def setphone(self,phone):
        self.__phone = phone

    def getmobile_phone(self):
        return self.__mobile_phone

    def setmobile_phone(self, mobile_phone):
        self.__mobile_phone = mobile_phone

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age

    def getstate(self):
        return self.__state

    def setstate(self,state):
        self.__state = state

    def contract(self):
        print("Se ha definido el contrato")