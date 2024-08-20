class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def roots(self) -> tuple[float] | tuple[float, float]:
        discriminant: float = self.b**2 - (4*self.a * self.c)
        if discriminant == 0:
            root: float = -self.b/(2*self.a)
            return (root,)
        else:
            root_1: float = (-self.b + discriminant**0.5)/(2*self.a)
            root_2: float = (-self.b - discriminant**0.5)/(2*self.a)
            return root_1, root_2


prueba = Quadratic(1, 7, 13)
print(prueba.roots())
