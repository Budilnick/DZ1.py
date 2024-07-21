def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c=[1, 2, 3])

value_list = [1, 'String', True]
value_dict = {'a':1, 'b':'String', 'c':True}
print()

print_params(*value_list)
print_params(**value_dict)

values_list_2 = [14.14, 'строка']
print_params(*values_list_2, 42)
