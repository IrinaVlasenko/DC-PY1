list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0 # индекс, соответствующий максимальному элементу
for current_index, current_number in enumerate(list_numbers): # перебираем пары списка индекс-значение
    if current_number > list_numbers[max_index]: # если текущее значение больше максимального
        max_index = current_index # записываем новое значение индекса
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index] # меняем местами элементы

print(list_numbers)
