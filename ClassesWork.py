#class Fruit(object):

    #def __init__(self):
        print ("starting Fruit class")

    def nutrition(self):
        print ("Fruit nutrion")

    def color(self):
        print ("Color class")

    def shape(self):
        print("Fruit shape")


class Apple(Fruit):

    def __init__(self):
        super(Apple, self).__init__()

    def nutrition(self):
        print("Apple's' nutrition")

    def color(self):
        print("Apple's color")


Kiwi = Fruit()


Golden = Apple()


Kiwi.nutrition()
Kiwi.color()

Golden.nutrition()
Golden.color()
Golden.shape()
