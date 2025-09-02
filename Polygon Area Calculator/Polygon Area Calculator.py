


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        shape = ''
        if self.width<=50 and self.height<=50:
            for i in range(self.height):
                for j in range(self.width):
                    shape += "*"
                shape += '\n'
            return shape
        else:
            shape+='Too big for picture.'
            return shape

    def get_amount_inside(self,shape):
        temp1=self.width//shape.width
        temp2=self.height//shape.height
        return temp1*temp2

    def __str__(self):
        # 'Rectangle(width=5, height=10)'
        str=f"Rectangle(width={self.width}, height={self.height})"
        return str


class Square(Rectangle):
    def __init__(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.width=side
        self.height=side
    def __str__(self):
        # 'Rectangle(width=5, height=10)'
        str=f"Square(side={self.height})"
        return str
    def set_width(self,width):
        self.set_side(width)
    def set_height(self,height):
        self.set_side(height)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(51)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(50)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
sq.set_width(2)


rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))