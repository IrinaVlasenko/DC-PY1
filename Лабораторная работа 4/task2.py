def get_count_char(str_):  # Функция для подсчета количества элементов строки
    letter_dict = {}
    DEFAULT_COUNT = 0
    for current_symbol in str_.lower():  # Перебираем символы строки, переведенной в нижний регистр
        if current_symbol.isalpha():  # Проверяем, что символ является буквой
            letter_dict[current_symbol] = letter_dict.get(current_symbol, DEFAULT_COUNT) +1
    return letter_dict

def get_freq_char(dict_):  # Функция для подсчета процентного соотношения элементов ко всем символам
    dict_freq = {}
    total_count = sum(dict_.values())  # Считаем общее количество всех символов
    for letter in dict_:  # Перебираем символы словаря
        dict_freq[letter] = round((dict_.get(letter) / total_count), 2)  # Заменяем кол-во символов на их процентное отношение
    return dict_freq

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
