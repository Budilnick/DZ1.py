def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)


print(summa(999))
"""

stack = []
stack.append(1)
print('dobavili element', stack)
stack.append(1)
print('dobavili element', stack)
stack.append(3)
print('dobavili element', stack)
print(stack)
stack.pop()
print('ubrali element', stack)
stack.pop()
print('ubrali element', stack)
stack.pop()
print('ubrali element', stack)
print(stack)"""