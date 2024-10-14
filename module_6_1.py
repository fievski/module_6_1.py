class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Медведь')
a2 = Mammal('Собакен')
p1 = Flower('Листок')
p2 = Fruit('Лимон')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


# class Human:
#     head = True
#
#     def say_hello(self):
#         print('Привет')
#
# class Student(Human):
#     head = False
#     def about(self):
#         print('Я студент')
#
#     def say_hello(self):
#             print('Привет')
#
# class Teacher(Human):
#     pass
#
# #human = Human()
# student = Student()
# teacher = Teacher()
# teacher.say_hello()
# print(student.head)
#


