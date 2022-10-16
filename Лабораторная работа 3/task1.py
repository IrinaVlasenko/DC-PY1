src = not False and True or False and not True

# result = True and True or False and False # Избавляемся от отрицаний
# result = True or False # Избавляемся от логического "И"
# result = True # Избавляемся от логического "ИЛИ"

result = True

print(src == result)
