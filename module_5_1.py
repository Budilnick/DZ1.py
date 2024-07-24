class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print('Такого этажа не существует')
        for i in range(1, new_floor + 1):
            if self.numbers_of_floors >= new_floor >= 1:
                print(i)
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
