class Factory():
    def __init__(self,fac_name,fac_num,fac_loc,fac_type) -> None:
        self.name = fac_name
        self.fac_num = fac_num
        self.fac_loc = fac_loc
        self.fac_type = fac_type

    def Dispaly(self):
        print(f"Factory name : {self.name}\n"
              f"Factory Number : {self.fac_num}\n"
              f"Location : {self.fac_loc}\n"
              f"Prodution Type : {self.fac_type}")
        print("Product Available")        
        
class Product(Factory):
    def __init__(self, fac_name, fac_num, fac_loc, fac_type, name_pro1 ,name_pro2 , name_pro3,) -> None:
        super().__init__(fac_name, fac_num, fac_loc, fac_type)
        self.name_pro1 = name_pro1
        self.name_pro2 = name_pro2
        self.name_pro3 = name_pro3

    def products(self):
        print(f"Product No 1. {self.name_pro1}\n"
              f"Product No 2. {self.name_pro2}\n"
              f"Product No 3. {self.name_pro3}")
        

obj = Product("Acer Lap Top",86,"Kerala","Lap tops And Electronics","Acer Swift Go evo : 64'000","Acer Aspire 3 Intel : 55'000","Acer Nitro : 77'000")
obj.Dispaly()
obj.products()