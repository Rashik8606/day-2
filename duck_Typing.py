# Duck Typing

class Animal():
    def perform(self):
        print("Animal perform in the circus")

class Human():
    def perform(self):
        print("Human perform in the circus")

class Circus():
    def Play(self,animal:Animal):
        animal.perform()

akaash = Human()
cat = Animal()
cat.perform()
akaash.perform()