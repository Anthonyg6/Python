# A Class is a blue print that will construct and make up an objects guts once the class has been instantiated within the object
# Below is a class blue print of a recipe


class Recipe:
    def __init__(self, name, ingredients, cook_time):
        self.name = name
        self.ingredients = ingredients
        self.cook_time = cook_time


# By storing the class Recipe within a variable that is what instantiates the object and turns that variable into an object
pizza = Recipe("Pizza", "Cheese, dough, marinara sauce, pepporini", 10)

# print(pizza.name, pizza.ingredients, pizza.cook_time)


class Courses:
    # Instance object which can be access by calling the classname.attributeName which in this case would be "print(Courses.website)"
    website = "https://bottega.com"

    def __init__(self, name):
        self.name = name


Javascript = Courses('Javascript')
python = Courses('Python')

print(Javascript.name)
print(Courses.website)

print(python.name)
print(Courses.website)
