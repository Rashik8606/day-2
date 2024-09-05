#Private verible
class Human():
    def __init__(self) -> None:
        self.__name = "Rashik"
        self.__age = 22
        self.__place = "Kochi"

    def __info(self):
        print(f"Name : {self.__name}\n"
              f"Age : {self.__age}\n"
              f"Place : {self.__place}")
        
    def Display(self):
        self.__info()
        
o = Human()
print(o._Human__age)  #''' Name Mangling'''#
#obj.__info()    #this will shows error, because we need as public access to get private method 
o.Display() #we have to declare a new public method to access an private method opration