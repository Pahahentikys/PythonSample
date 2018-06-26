class Auto:

    def __init__(self, color, cost, name):
        self.__color = color
        self.__cost = cost
        self.__name = name

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Имя не должно быть пустым!")

    def set_color(self, color):
        self.__color = color

    def set_cost(self, cost):
        self.__cost = cost

    def show_info(self):
        # print("Информация об автомобиле: ", self.__name, self.__cost, self.__color)
        print("Информация об автомобиле: {2} {1} {0}".format(self.__name, self.__cost, self.__color))