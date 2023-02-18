class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SuvatCalculator:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def calculate(self, s, u, v, a, t):
        self.insert(s)
        self.insert(u)
        self.insert(v)
        self.insert(a)
        self.insert(t)

        if s is None:
            s = (u*t) + (0.5*a*t*t)
        elif u is None:
            u = (s - (0.5*a*t*t)) / t
        elif v is None:
            v = u + (a*t)
        elif a is None:
            a = (v - u) / t
        elif t is None:
            t = (v - u) / a

        return s, u, v, a, t

calculator = SuvatCalculator()
s, u, v, a, t = calculator.calculate(None, 0, 10, 2, 5)
print("s = ", s, "u = ", u, "v = ", v, "a = ", a, "t = ", t)
