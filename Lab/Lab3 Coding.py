def twos_powers(n):
    for i in range(n):
        yield 2**i


def reverse_twos_powers(n):
    for i in range(n):
        yield 1 / 2 ** i


class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str

    def __add__(self, other):
        result = ""
        carry = 0
        if len(self.data) < len(other.data):
            self.data, other.data = other.data, self.data
        for i in range(1, len(self.data) + 2):
            if i == len(self.data) + 1:
                if carry == 0:
                    return UnsignedBinaryInteger(result)
                else:
                    result = str(carry) + result
                    return UnsignedBinaryInteger(result)
            if i > len(other.data):
                submit = int(self.data[-i]) + carry
            else:
                submit = int(self.data[-i]) + int(other.data[-i]) + carry
            if submit > 1:
                number = submit % 2
                carry = 1
            else:
                number = submit
                carry = 0
            result = str(number) + result

    def decimal(self):
        return sum([int(self.data[i]) * 2 ** (len(self.data) - i - 1)
                    for i in range(len(self.data))])

    def __lt__(self, other):
        if self.decimal() < other.decimal():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.decimal() > other.decimal():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.decimal() == other.decimal():
            return True
        else:
            return False

    def is_twos_power(self):
        for i in range(1, len(self.data)):
            if self.data[i] != '0':
                return False
        return True

    def largest_twos_power(self):
        return 2 ** (len(self.data) - 1)

    def __repr__(self):
        return "0b" + self.data

    def __or__(self, other):
        result = ""
        if len(self.data) < len(other.data):
            self.data, other.data = other.data, self.data
        for i in range(1, len(self.data) + 1):
            if i > len(other.data):
                result = str(self.data[-i]) + result
            else:
                result = str(int(self.data[-i]) | int(other.data[-i])) + result
        return UnsignedBinaryInteger(result)

    def __and__(self, other):
        result = ""
        if len(self.data) < len(other.data):
            self.data, other.data = other.data, self.data
        for i in range(1, len(other.data) + 1):
            result = str(int(self.data[-i]) & int(other.data[-i])) + result
        while len(result) > 1:
            if result[0] == "0":
                result = result[1:]
            else:
                break
        return UnsignedBinaryInteger(result)


b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("b1 is: ", b1)  # 0b10011
print("b2 is: ", b2)  # 0b100
b3 = b1 + b2
print("b3 is: ", b3)  # 0b10111
print("\nChecking decimal values:\n")
print(b1.decimal())  # 19
print(b2.decimal())  # 4
print(b3.decimal())  # 23
print("\nChecking comparisons:\n")
print(b1 < b2)  # False
print(b2 < b1)  # True
print(b1 > b2)  # True
print(b2 > b1)  # False
print(b1 + b2 == b3)  # True
print("\nChecking is_twos_power:\n")
print(b1.is_twos_power())  # False
print(b2.is_twos_power())  # True
print(b3.is_twos_power())  # False
print("\nChecking largest_twos_power:\n")
print(b1.largest_twos_power())  # 16
print(b2.largest_twos_power())  # 4
print(b3.largest_twos_power())  # 16
b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("\nTesting b1: ", b1, "b2: ", b2)
b3 = b1 | b2
b4 = b1 & b2
print(b1, "|", b2, "=", b3)  # 0b100
print(b1, "&", b2, "=", b4)
b1 = UnsignedBinaryInteger('1010')
b2 = UnsignedBinaryInteger('1001')
print("\nTesting b1: ", b1, "b2: ", b2)
b3 = b1 | b2
b4 = b1 & b2
print(b1, "|", b2, "=", b3)
print(b1, "&", b2, "=", b4)
