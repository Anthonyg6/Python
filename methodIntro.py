# class Fighter:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.damage = 10

#     def attack(self, other_guy):
#         other_guy.health = other_guy.health - self.damage
#         print()

#     def __str__(self):
#         return "{}: {}".format(self.name, self.health)


# anthony = Fighter('Anthony')
# jayce = Fighter('Jayce')

# print(anthony)


# print(anthony.name)
# print(jayce.name)

# jayce.attack(anthony)

# print(anthony.health)


# class Pet(object):
#     def my_method(self):
#         print('Hello I am a cat')


# cat = Pet()
# cat.my_method()

import random


class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = random.randint(1, 20)

    def attack(self, other_guy):
        other_guy.current_health = other_guy.health - self.damage
        print("{} attacks {}".format(self.name, other_guy.name))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)


Gus = Fighter("Gus")
Joey = Fighter("Joey")

print(Gus)
print(Joey)

Joey.attack(Gus)
print(("Gus takes") + str(Gus.damage) + ("points of damage!"))

print("Gus has" + str(Gus.current_health) + ("health points left"))
