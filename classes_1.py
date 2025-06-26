
class Dog:
    legs = 4
    weight = "10kg"
    has_teeth = True

    def __init__(self, name, age=1, owner="Strada", sound="Woof"):
        self.name = name
        self.age = age
        self.owner = owner
        self.bark_sound = sound

    def bark(self):
        print("{}!".format(self.bark_sound))

    def sniff(self, other_dog):
        print('Dog "{}" sniffed dog "{}"\'s ass'.format(self.name, other_dog.name))

    def combined_age(self, other_dog):
        print(self.age + other_dog.age)

    def convince(self, other_dog):
        other_dog.owner = self.owner

    def __str__(self):
        return "Dog: {}, age={}, that belongs to {}.".format(self.name, self.age, self.owner)

    def __repr__(self):
        return 'Dog("{}", age={}, owner="{}")'.format(self.name, self.age, self.owner)

d1 = Dog("Spot", 10, "Mihai")
d2 = Dog("Shadow", age=3, owner="Oana", sound="WOOOOF")
# d3 = Dog: Spot, age=10, that belongs to Mihai.
d3 = Dog("Grabby", age=10, owner="Oana", sound="AwwwwOOOOOOooo")

dog_park = [d1, d2, d3]
print(dog_park)

d1.bark()
d1.sniff(d2)
d1.convince(d2)
d1.combined_age(d2)
# print(d2)



for d in dog_park:
    d.bark()

d1.address = "Brasov, Padurea Jepilor"
print(d1.address)
d1.legs = 3

# print(d1)
# print(d2)
# str_repr1 = str(d1)
# print(str_repr1)


# print(d1.legs)
# print(d2.legs)
# print(Dog.legs)
#
# print(d1)
# print(d2)
# print(isinstance(d2, Dog))
# print(d3 is d2)

# print(d1.name)
# print(d2.name)

class Cat:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.fur_density = "100"

    def meow(self):
        print("Meoooww!")

    def __str__(self):
        return "Cat: '{}' owned by '{}'".format(self.name, self.owner)

    def __repr__(self):
        return "Cat('{}', '{}')".format(self.name, self.owner)

c1 = Cat("Kitty", "Mihai")
c2 = Cat("Jade", "Mihai")

park = [d1, d2, d3, c1, c2]
print(park)

for animal in park:
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()


class Park:
    def __init__(self):
        self.park_area = []

    def add_animal(self, animal):
        self.park_area.append(animal)

    def animal_sounds(self):
        # Calls each animal's sound method!
        for animal in self.park_area:
            if isinstance(animal, Dog):
                animal.bark()
            elif isinstance(animal, Cat):
                animal.meow()

new_park = Park()
new_park.add_animal(d1)
new_park.add_animal(d2)
new_park.add_animal(d3)
new_park.add_animal(c1)
new_park.add_animal(c2)

print(new_park.park_area)
new_park.animal_sounds()

# new_park2 = Park()
# new_park2.add_animal(d2)


class DogPark:
    def __init__(self):
        self.park_area = []

    def add_dog(self, dog):
        if isinstance(dog, Dog):
            self.park_area.append(dog)
        else:
            print("This is not a dog!")
            print(dog)


park2 = DogPark()
print("Adding dogs to park:")
park2.add_dog(d1)
park2.add_dog(d2)
park2.add_dog(c1)

print(park2.park_area)


class AnimalPark:
    def __init__(self, name, limit=10):
        self.name = name
        self.limit = limit

        self.dog_area = []
        self.other_animals_area = []

    def add_animal(self, animal):
        # If the animal is a dog, add it to the dog area. Otherwise, put it in the other animals area.
        # If we already have x animals, x being the self.limit value, we won't add any more.
        if len(self.dog_area) + len(self.other_animals_area) < self.limit:
            if isinstance(animal, Dog):
                self.dog_area.append(animal)
            else:
                self.other_animals_area.append(animal)
        else:
            print("Park is full! Can't add any more animals. Park limit {}.".format(self.limit))
    def __str__(self):
        result = {
            "dogs": self.dog_area,
            "other animals": self.other_animals_area
        }
        return str(result)


print("Creating new park.")
park3 = AnimalPark("Park Titulescu", 2)
print("Adding animals to new park.")
park3.add_animal(d1)
park3.add_animal(c1)
park3.add_animal(c2)

print(park3)
