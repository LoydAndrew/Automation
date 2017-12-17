


class Car(object):
    wheels=4


    def __init__(self, name,type):
        self.type = type
        self.name = name
    def info(self):

        print("Type of car is a %s %s " % (self.type, self.name))

car1 = Car('bmw','cedan')
car1.info()
print (car1.wheels)
car2 = Car('mers','jeep')
car2.info()
car1.wheels = 2
print (car1.wheels)
print (car2.wheels)
