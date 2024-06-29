class Aninimal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Aninimal):
    pass


class Predator(Aninimal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


bear = Mammal('Медведь')
apple = Fruit('землянику')
bear.eat(apple)
