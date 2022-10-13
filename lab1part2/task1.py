class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def per(self):
        return 2*(self.__width+self.__length)

    def area(self):
        return self.__width*self.__length

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError()
        if val <= 0 or val > 20:
            raise ValueError()
        self.__length = val

    @width.setter
    def width(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError()
        if val <= 0 or val > 20:
            raise ValueError()
        self.__width = val

    def __str__(self):
         return f'Lendth = {self.length} Width = {self.width}'


rectangle1 = Rectangle(4, 6)
print(rectangle1)
rectangle1.width = 10
print(rectangle1)