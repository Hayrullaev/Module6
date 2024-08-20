import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * 12
            else:
                self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in [r, g, b]:
            if not (isinstance(color, int) and 0 <= color <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        # cond_1 = len(self.__sides) == len(*sides)

        if isinstance(self, Cube):
            cond_1 = len(sides) == 1
        else:
            cond_1 = len(sides) == self.sides_count
        cond_2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond_1 and cond_2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * 12
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=tuple, *sides):
        super().__init__(color, sides)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * math.pow(self.__radius, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=tuple, *sides):
        super().__init__(color, sides)
        # sp = self.__len__() / 2
        # self.height = (2 ** (sp(sp - self.__sides[0])(sp - self.__sides[1])(sp - self.__sides[2]))) / 2 * sp
        self.height = 1000

    def get_square(self):
        return 10


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=tuple, *sides):
        super().__init__(color, sides)

    def get_volume(self):
        return 50


# круг
circle1 = Circle((200, 200, 100), 10)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square())
print('радиус:', circle1.get_radius())
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 3)
print('цвета:', circle1.get_color())
circle1.set_color(-1, 200, 3)
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 300.0)
print('цвета:', circle1.get_color())
circle1.set_sides(10)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square())  # не меняет площадь
print('радиус:', circle1.get_radius())  # не меняет радиус
circle1.set_sides(10, 8)
print('стороны:', circle1.get_sides())

print('\n\n\n\n\n')

# треугольник
fig = Triangle((200, 200, 100), 10)
print('стороны:', fig.get_sides())
print('прощадь:', fig.get_square())  # + получение высоты треугольника
print('цвета:', fig.get_color())

fig = Triangle((200, 200, 100), 10, 7, 9)
print('стороны:', fig.get_sides())
fig.set_sides(1)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('стороны:', fig.get_sides())

print('\n\n\n\n\n')
# куб
fig = Cube((200, 200, 100), 10, 12)
print('стороны:', fig.get_sides())
print('прощадь:', fig.get_volume())
print('цвета:', fig.get_color())

fig = Cube((200, 200, 100), 10)
print('стороны:', fig.get_sides())
fig.set_sides(50)
print('стороны:', fig.get_sides())
fig.set_sides(-100)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('стороны:', fig.get_sides())
