class Attribute():
    def __init__(self) -> None:
        self.name = "Public Attribute"
        self._name = "Protected Attribute"
        self.__name = "Private Attribute"

    def public_method(self):
        print("Public Method")
    
    def _Protected_Method(self):
        print("Protected Method")

    def __Private_Method(self):
        print("Private Method")

Obj = Attribute()
print(Obj.name)
print(Obj._name)
print(Obj._Attribute__name)
print("_____")
Obj.public_method()
print(Obj._Protected_Method())
Obj._Attribute__Private_Method()  #Name Mangiling
