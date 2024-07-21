a = [True, False, False]
print(any(a))
b = [0, 0, 0]
print(any(b))
c = ' '
print(any(c))
d = [True, False]
print(all(d))
print(type(d))
print(isinstance(d, list))
print(type(d) is list) # равнозначно (tyre(d) == list)

a = [1, 1, 1]
d = [1, 1, 1]
c = d
print(id(a))
print(id(d))
print(id(c))
print(a is d)  #разные id объекта, потому False
print(c is d)
