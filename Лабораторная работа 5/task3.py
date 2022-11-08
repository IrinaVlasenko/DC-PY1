import random

size_list = 15
number_start = -10
number_end = 10


def get_unique_list_numbers() -> list[int]:
    list_unique = []
    while len(list_unique) != size_list:  # Выполняем цикл, пока длина последовательности не станет = 15
        i = random.randint(number_start, number_end)
        if i not in list_unique:  # Проверяем, что случайного числа еще нет в последовательности
            list_unique.append(i)  # Добавляем уникальное число в последовательность
    return list_unique


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
