def print_initial_array(array):
    print("=== Массив до сортировки ====")
    for item in array:
        print(item)

# Количество сравнений для массива из n будет:
# (n-1) + (n-2) + ... + 1
# n(n-1) / 2
# n^2/2 - n/2 => O(n^2)
# Для Bubble Sort количество сравнений будет:
# с массивом из 5 элементов; 4 + 3 + 2 + 1 = 10
def bubble_sort(input_array):
    print("\n" + "*** Buble Sort ***" + "\n")
    print_initial_array(input_array)
    print("=== Массив после сортировки ====")
    for i in range(len(input_array) - 1):
        for j in range(0, input_array[i] - 1):
            # Тут можно посчитать сравнение ключей массива.
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j + 1]
                input_array[j + 1] = input_array[j]
                input_array[j] = temp
                # Идут пересылки элементов массива
                # print("Процесс сортировки: ", input_array)
    # Итоговый результат сортировки
    print(input_array)

# Худший случай сравнении и перстановок: O(n^2). Все элементы остортированы в обратном порядке*
# Средний случай сравнении и перстановок: O(n^2).
# Лучший случай: O(n) - сравнении и O(1) - перстановок. Все элементы уже отсортированы*
def insertion_sort(input_array):
    print("\n" + "*** Insertion Sort ***" + "\n")
    print_initial_array(input_array)
    print("=== Массив после сортировки ====")
    # Во внешнем цикле идём от 1, т.к. постепенно наполняем массив от начального
    # новыми элементами и сравниваем их.
    for i in range(1, len(input_array)):
        j = i
        while j > 0 and input_array[j] < input_array[j-1]:
            temp = input_array[j-1]
            input_array[j-1] = input_array[j]
            input_array[j] = temp
            j -= 1
            # print(input_array)
    print(input_array)

def merge(input_array, end_1, end_2):
    i = 0
    j = end_1
    k = 0
    temp = []

    while i < end_1 and j < end_2:

        if(input_array[i] < input_array[j]):
            temp[k] = input_array[i]
            i += 1
            k += 1

        else:
            temp[k] = input_array[j]
            j += 1
            k += 1

    while i < end_1:
        temp[k] = input_array[i]
        i += 1
        k += 1

    while j < end_2:
        temp[k] = input_array[j]
        j += 1
        k += 1

    for i in range(0, i < end_2, i + 1):
        input_array[i] = temp[i]

def merge_sort(input_array):
    print("\n" + "*** Merge Sort ***" + "\n")
    print_initial_array(input_array)
    print("=== Массив после сортировки ====")
    i = 1
    for i in range(1, i < len(input_array), 2 * i):
        j = 0
        for j in range(0, j < len(input_array) - i, j + 2 * i):
            merge(input_array[j], i, 2 * i)



array = [5, 3, 8, 1, 5]

array_for_insertion_sort = [9, 3, 2, 10, 4]

array_for_merge_sort = [4, 2, 1, 8, 6, 3, 7, 5]

bubble_sort(array)

# insertion_sort(array_for_insertion_sort)

# merge_sort(array_for_merge_sort)