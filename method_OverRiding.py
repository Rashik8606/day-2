#method Over Riding

class function():
    def func1(self):
        print("One is Working on A")
    def fun(self):
        print("Two is working A")
class function1(function):
    def func2(self):
        print("Two is working on B")
    def fun(self):
        print("Two is Working on B")
        super().fun()

obj = function1()
obj.func2()
obj.fun()