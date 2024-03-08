class Circle:
    def __init__(self, r: float):
        assert r > 0
        self.r =r

    def perimeter(self):
        from math import pi
        return pi * 2 * self.r

    def area(self):
        from math import pi
        return pi * (self.r ** 2)

