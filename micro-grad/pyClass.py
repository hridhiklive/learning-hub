class Value:
    def __init__(self, data):
        self.data = data
        self.grad = 0.0

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        return Value(self.data + other.data)

    def __sub__(self, other):
        return Value(self.data - other.data)

    def __mul__(self, other):
        return Value(self.data * other.data)

    def __truediv__(self, other):
        return Value(self.data / other.data)
    
p = Value(9)
q = Value(3)
a = p + q
b = p - q
c = p * q
d = p / q

print(f"a: {a}, b: {b}, c: {c}, d: {d}")