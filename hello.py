print("Hello, Python!")

while True:
    name = input()

    if name.lower() == "n":
        print("Пока-пока!")
        break

    if name == "":
        print("Введите имя!")
    else:
        print("Hello, " + name + "!")






