def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params( b=25 )
print_params( c=[123] )

values_list = [1, 'str', True]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
print()

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'Hallo']
print_params(*values_list_2, 42)