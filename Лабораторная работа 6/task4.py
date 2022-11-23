import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename) -> list[dict]:
    list_dict = []  # Создаем пустой список
    with open(filename) as f:  # Открываем файл в режиме чтения
        list_ = [line.rstrip().split(",") for line in f]  # Создаем список списков строк, разбитых по разделителю ","
        list_headers = list_[0]  # Создаем список заголовков
        list_data = list_[1:]  # Создаем список списков с данными таблицы
        for line_value in list_data:
            dict_ = {list_headers[i]: line_value[i] for i in range(len(list_headers))}  # Создаем словарь для строки
            list_dict.append(dict_)  # Добавляем словарь в список

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
