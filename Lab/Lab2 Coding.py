class Polynomial:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if (len(self.data) < len(other.data)):
            (self.data, other.data) = (other.data, self.data)
            new = []
            for i in range(len(self.data)):
                if (i < len(other.data)):
                    new.append(self.data[i] + other.data[i])
                else:
                    new.append(self.data[i])
        return Polynomial(new)

    def __call__(self, number):
        return self.data[number - 1]

    def __repr__(self):
        return " + ".join([str(self.data[len(self.data) - 1 - i]) + 'x^'
                           + str(len(self.data) - 1 - i)
                           for i in range(len(self.data))])

    def __mul__(self, other):
        new = [0 for i in range(len(self.data) + len(other.data) - 1)]
        for i in range(len(self.data)):
            for j in range(len(other.data)):
                new[i + j] += self.data[i] * other.data[j]
        return Polynomial(new)

    def derive(self):
        new = []
        for i in range(1, len(self.data)):
            new.append(i * self.data[i])
        return Polynomial(new)
