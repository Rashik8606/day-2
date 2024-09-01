#Method Over LOading
#By defult Argument

class add_num():
    def find_Sum(self,num1,num2,num3=0):
        print(num1+num2+num3)

obj = add_num()
obj.find_Sum(10,20)