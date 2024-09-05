class Animal():
    def __init__(self) -> None:
        self._name = "Flexi"
        self.name = "Sarath"
        self._year = 2
        self.type = "Persian"

obj = Animal()
print(obj._name,obj.name)