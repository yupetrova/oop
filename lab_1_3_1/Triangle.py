class Triangle:
    def __init__(self, a: float, b: float, c: float):
        edges = [a, b, c]
        edges.sort()
        a, b, c = edges
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c)

    def area(self) -> float:
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
