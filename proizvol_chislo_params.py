#def test_func(*params):
#    print('тип', type(params))
#    print('аргумент', params)
#
#
#test_func(1, 2, 3, 4)

def summator(txt, *values, type='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type}'


print(summator('сумма чисел: ', 1, 2, 3, 4, type="summator"))


def info(**values):
    print('тип', type(values))
    print('аргумент', values)
    for key, values in values.items():
        print(key, values)

        
info(name='denis', course='python')