class Rectangle:
    def __init__(self, a: float, b: float):
        edges = [a, b]
        edges.sort()
        a, b = edges
        assert b > 0   #перевірка чи менша сторона невід'ємна
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b
