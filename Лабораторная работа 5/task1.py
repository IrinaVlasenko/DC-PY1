from pprint import pprint

number_end = 15

list_dic = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(number_end+1)]

pprint(list_dic)
