class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """工厂方法 创建一个半径为1的圆"""
        return cls(1)

    @staticmethod
    def pi():
        return 3.1415926535


c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 2
print(c.area)
# c.area = 100 会报错，因为没有area这个attribute
c.cylinder_volume(height=4)
# c.radius = -1 会raise一个error
c = Circle.unit_circle()
print(c.radius)
print(c.pi())
