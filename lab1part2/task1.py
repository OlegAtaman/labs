class Rectangle:
    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    def per(self):
        return 2*(self.width+self.length)

    def area(self):
        return self.width*self.length

    def length(self):
        return self.length

    def width(self):
        return self.width

    def set(self, width, length):
        if length >= 0.0 and length <= 20.0 and width >= 0.0 and width <= 20.0:
            self.width = width
            self.length = length
        else:
            print('ERROR')


square = Rectangle()
print(square.per())
print(square.area())
square.set(44, 20)
print(square.per())
print(square.area())