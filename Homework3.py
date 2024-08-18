class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)  # Вызов метода run() класса Horse
        super().fly(dy)  # Вызов метода fly() класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


pegaus = Pegasus()
p2 = Eagle()
print(pegaus.get_pos())
pegaus.move(20, 15)
print(pegaus.get_pos())
pegaus.move(21, 20)
print(pegaus.get_pos())

pegaus.voice()
