class Trapeze:
    def __init__(self, a: float, b: float, c: float, d: float):
        assert a > 0 and c > 0 and b > 0 and d > 0
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return (self.a + self.b + self.c + self.d)

    def area(self) -> float:
        return 0.5 *  (self.a + self.b)* self.d