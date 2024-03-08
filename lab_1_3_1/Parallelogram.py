class Parallelogram:
    def __init__(self, a: float, b: float, h: float):
        assert a > 0 and b > 0 and h > 0
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.h