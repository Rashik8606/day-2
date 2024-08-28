class employe():
    def __init__(self) -> None:
        self.name = " "
        self.age = 0
        self.salary = 0
        self.company = " "

    def employe_name(self):
        self.name=input('enter employe name --->')
        self.age=int(input('enter age -->'))
        self.salary=int(input('enter employe salary -->'))
        self.company=input('enter company name -->')

    def emplye_printed(self):
        print(f"employe name : {self.name}. age : {self.age}. salary {self.salary}. working {self.company}")

emp = employe()
emp.employe_name()
emp.emplye_printed()