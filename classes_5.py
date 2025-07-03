
# mostenire:

class Animal:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def make_sound(self):
        print("{}: BluuruurB!".format(self.name))

class Dog(Animal):
    def make_sound(self):
        print("{}: Welcome to the land of the dead!".format(self.name))

    def bark(self):
        print("WOOOF!")

class Cat(Animal):
    def make_sound(self):
        print("{}: Meow!".format(self.name))


class Bacteria:
    def action(self):
        print("Bacteria eats organic matter.")

class Prokaryote(Bacteria):
    def action(self):
        print("Prokaryote is part of a larger organism")


a1 = Animal("5kg", "Jellyfish")
a1.make_sound()

class Park:
    def __init__(self):
        self.park_area = []

    def add_animal(self, animal_param1):
        if isinstance(animal_param1, Animal):
            self.park_area.append(animal_param1)
        else:
            print("This is not an animal!")
            print(animal_param1)

    def animal_sounds(self):
        for animal in self.park_area:
            animal.make_sound()

p1 = Park()

dog1 = Dog("99999kg", "Cerberus")
dog1.make_sound()
dog1.bark()

p1.add_animal(dog1)

bact1 = Bacteria()
prok = Prokaryote()
p1.add_animal(bact1)
cat1 = Cat("5kg", "Link")
cat2 = Cat("5kg", "Zelda")
cat3 = Cat("5kg", "Zip")

p1.add_animal(cat1)
p1.add_animal(cat2)
p1.add_animal(cat3)

p1.add_animal(prok)

print(p1.park_area)
print("Making sounds!")
p1.animal_sounds()


