# Поиск повторяющихся элементов и их удаление из списка.
def del_repeat_elements(list):
    print("\n" + "=== Удаление дубликатов из списка ===" +  "\n")
    print("Старый список: ", list)
    unique_list = []
    for item in range(len(list)):
        if list[item] not in unique_list:
            print("Новый уникальный элемент в списке: ", list[item])
            unique_list.append(list[item])
    print("Без дубликатов: ", unique_list)
    return unique_list

# Поиск максимального элемента в списке
def find_max_elem(list):
    print("\n" + "=== Поиск максимума в списке ===")
    print("\n" + "Набор элементов в спике: ", list)
    max_element = list[0]
    for item in range(1, len(list)):
        if list[item] > max_element:
            print("Новый максимальный элемент: ", list[item])
            max_element = list[item]
    print("\n" + "Самый крупный элемент списка: ", max_element)
    return max_element

# Сумма элементов в списке
def sum_of_elements(list):
    print("\n" + "=== Сумма элементов списка ===" + "\n")
    sum = 0
    for item in range(len(list)):
        sum += list[item]
    print(sum)
    return sum



# list = [2, 2, 3, 1, 4]
# list = [2, 3, 2, 1, 4]
list_repeat_elems = [2, 3, 8, 5, 4, 4, 10, 7, 5, 7]

del_repeat_elements(list_repeat_elems)

find_max_elem(list_repeat_elems)

sum_of_elements(list_repeat_elems)
