class company():
    def __init__(self,name,com_rank,com_dic,com_loc):
        self.name = name
        self.com_rank = com_rank
        self.com_dic = com_dic
        self.com_loc = com_loc

class employe():
    def __init__(self,name,id,age,comp:company):
        self.name = name
        self.id = id
        self.age = age
        self.company = comp

    def display(self):
        print(f"Name : {self.name}\nemploye id : {self.id}\nage : {self.age}\nCompany name :{self.company.name}\nCompany Rank :{self.company.com_rank}\n"
              f"Founder name : {self.company.com_dic}\nCompany location : {self.company.com_loc}")

details_com = company("Google",3,"Sundar pichai","Delhi")
details = employe("Rashik",8606,22,details_com)
details.display()