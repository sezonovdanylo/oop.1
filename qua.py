class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")

    def dis(self):
        print("кщрені рівняння:")
        d = self.b**2 - 4*self.a*self.c
        if self.a ==0:
            if self.b == 0:
                if self.c == 0:
                    print('Inf')
                else:
                    print("[]")
            else:
                print(self.c / self.b *(-1))
        else:
            if d < 0:
                print("[]")
            if d ==0:
                print(self.b / (-2* self.a))
            if d >0:
                print((-1*self.b + d**0.5)/(2*self.a), (-1*self.b - d**0.5)/(2*self.a) )




