my_dict = {'Vanya': 1985, 'Lena': 1992, 'Artem': 2017, 'Sergey': 1982}
print('Словарь:', my_dict)
print('Существующее значение: ', my_dict.get('Vanya'))
print('Несуществующее значение: ', my_dict.get('Sveta', 'Нет его'))
my_dict['Sveta'] = 1991
my_dict['Maxim'] = 1983
my_dict.pop('Vanya')        #1й вариант
del my_dict['Sergey']       #2й вариант
print('Модифицированный словарь', my_dict)
my_set = {12, 12, 'root', True, 'root', True, 12}
print('множество', my_set)
my_set.add(13)
my_set.add('torch')
my_set.remove(12)
print('Модифицированное множество', my_set)