class person:
    def __init__(self, age, height, name):
        self.age = age
        self.height = height
        self.name = name

    def eat(self):
        return "I love food!"
    
    def drive(self):
        return "I drive a Probox!"
    
    def start(self, car):
        car.drive()

        
 # inheritance   
class child(Parent):
    def__init__(self, age, height, name):
        parent.__init__(self)





myperson = person(29, 169, "Jack Doe")

print(myperson.age)
print(myperson.height)
print(myperson.name)
print(myperson.eat())
print(myperson.drive())

