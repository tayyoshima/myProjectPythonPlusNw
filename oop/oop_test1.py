class Person:
    #Attribute
    name = "Paisit"
    lastN = "W."
    __age = 27 #private
    _id = "123456" #protected
    print(__age)
    #Method/Behavior
    def __init__(self):
        print("Start") #Constructor
    def __sayHello(self):
        print("Hello")
    def run(self):
        print("I running")

class Programmer(Person):
    name = 'John'
    salary = 100000
    def program(self):
        print("Coding")

#human2 = Programmer()
#print(human2.name)

human1 = Person() #Create object
print(human1._id) #call attribute name
#human1.sayHello() #call function sayHello()