class Vehicle():
    def __init__(self,company,model,colur,fuel) -> None:
        self.company = company
        self.model = model
        self.colur = colur
        self.fuel = fuel

    def start_engine(self):
        print("starting engine")

    def changing_gear(self):
        print("changing gears")

class car(Vehicle):
    def __init__(self, company, model, colur, fuel,body_type) -> None:
        super().__init__(company, model, colur, fuel)
        self.body_type = body_type
    def sun_roof(self):
        print("opening sun roof")

obj = car('bmw','m1','black','diesel',"suv")
obj.start_engine()
obj.changing_gear()
obj.sun_roof()
