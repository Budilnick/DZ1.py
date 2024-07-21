immutable_var = (1, 2, True, "Zhiguli", 555)
print(immutable_var)
# immutable_var[0] = 3    Кортеж не поддерживает функцию замены  элемента кортежа, в отличие от списка
# print(immutable_var)    Решетку поставил, чтобы не выпадало ошибок
mutable_list = [1, 2, True, "Zhiguli", 555]
mutable_list[4] = 3
print(mutable_list)
