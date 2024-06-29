
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, model, engine_power, owner, color):
        self.__model = model
        self.__engine_power = engine_power
        self.owner = owner
        self.__color = color

    # Метод для получения модели автомобиля
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета автомобиля
    def get_color(self):
        if self.__color.lower() in Vehicle.__COLOR_VARIANTS:
            return f"Цвет: {self.__color}"
        else:
            raise ValueError('Некорректный цвет автомобиля')

    # Распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец:", self.owner)

    # Принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"
    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на:", new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, model, engine_power, owner, color):
        super().__init__(model, engine_power, owner, color)

    # Метод для получения информации о количестве пассажиров, которое может поместиться в автомобиль
    def get_passengers_limit(self):
        return f"Количество пассажиров: {Sedan.__PASSENGERS_LIMIT}"


Vehicle = Sedan('Hyndai Elantra VII', 128, "Shoh", "White")
Vehicle.print_info()

Vehicle.set_color('Pink')
Vehicle.set_color('BLACK')
Vehicle.owner = "Vova"

Vehicle.print_info()



