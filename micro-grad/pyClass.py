
class Value:
    def __init__(self, data,_children=(),_op='',label=''):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    

    def __sub__(self, other):
        out = Value(self.data - other.data, (self, other), '-') 
        return out
    

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), '*')

    def __truediv__(self, other):
        return Value(self.data / other.data, (self, other), '/')
    
  

