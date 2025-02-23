class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x,y,z

    @classmethod
    def from_points(cls, start, end):
        pass

    @classmethod
    def dot_product(cls, first, second):
        return first @ second

    @classmethod
    def cross_product(cls, first, second):
        pass

    def __getitem__(self, item):
        match item:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.z

        raise IndexError()

    def __setitem__(self, key, value):
        match key:
            case 0:
                self.x = value
                return
            case 1:
                self.y = value
                return
            case 2:
                self.z = value
                return

        raise IndexError()

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __next__(self):
        pass

    def __len__(self):
        return 3

    def __contains__(self, item):
        pass

    def __reversed__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number, self.z * number)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rdiv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


v1 = Vector(x=5, y=7, z=9)
v2 = Vector(x=2, y=3, z=4)

print(v1[2])

v1[1] = 85
for val in v1:
    print(val)

print(len(v1))

if v1 > v2:
    print('v1 > v2')

if v1 < v2:
    print('v1 < v2')

v3 = v1 + v2
print(v3)

print(abs(v1))

print(v1 * 5)
print(v1 @ v2)
print(Vector.dot_product(v1, v2))

#protocol итерация
# __getitem__
# __setitem__
# __iter__
# __next__

#protocol sequence
# __len__
# __contains__
# __reversed__

#comparison
# __eq__
# __lt__
# __gt__

#vector operations
# __add__
# __sub__
# __mult__ (scalar)
# __rdiv__
# __abs__

#classmethod
# scalar multiplication -> __mult__
# vector multiplication
# mixed multiplication -> vector + scalar

# string representation
# __str__
# __repr__

#dynamic property creation is forbidden
# __slots__ -> tuple()

