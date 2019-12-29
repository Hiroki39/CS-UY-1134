class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        else:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector([-i for i in self])
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            result = Vector([i * other for i in self])
        else:
            if (len(self) != len(other)):
                raise ValueError("dimensions must agree")
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
        return result

    def __rmul__(self, n):
        result = Vector([i * n for i in self])
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)
