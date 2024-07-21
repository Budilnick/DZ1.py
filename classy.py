class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age =+ 1
        print(f'У меня день рождения, мне теперь {self.age}')

den = Human('Денис', 22)
max = Human('Макс', 33)
max.birthday()


#den.say_info()
#max.say_info()


#print(den.name, den.age)
#print(max.name, max.age)