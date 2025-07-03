
# explaining decorators:

# closure
def func_generator():
    def inner_func():
        return 42

    return inner_func

# closure
generated_function = func_generator()
print(generated_function())


def logger_decorator(func):
    def wrapper():
        print("calling function!")
        func()
        print("function called! No problems detected!")
    return wrapper

@logger_decorator
def dog_barks():
    print("Woof!")

@logger_decorator
def cat_meows():
    print("Meow!")

dog_barks()
cat_meows()

user_is_logged_in = True

# login required decorator
def login_required(func):
    def wrapper():
        if user_is_logged_in:
            func()
        else:
            print("User must be authenticated!")
    return wrapper

@login_required
def change_username():
    # db.change_username("adrian", "faust")
    print("Adrian changed to Faust.")

change_username()


# End of decorator explanation
print("------END-------")

class MyClass():
    def __init__(self, name):
        self.name = name

    def met_1(self):
        print("Hello from object {}!".format(self.name))

    @staticmethod
    def method_static():
        print("Hello from static method itself!")

    @classmethod
    def class_method(cls):
        print("Hello from Class method!")
        print(cls)

m1 = MyClass("instanta 1")
m1.met_1()
# m2 = MyClass("instanta 2")
# m2.met_1()

MyClass.method_static()
MyClass.class_method()

class Dog:

    def __init__(self, name, age=1, owner="Strada"):
        self.name = name
        self.age = age
        self.owner = owner

    @classmethod
    def from_string(cls, string_arg1: str):
        name, age, owner = string_arg1.split("-")
        new_instance = cls(name, int(age), owner)
        return new_instance

dog1 = Dog("Cerberus", 99999999999, "Hades")
print(dog1.name)

dog2 = Dog.from_string("Cerberus-9999999999-Hades")
# print(type(dog2.age))
print(dog2.age)

# str1 = "Cerberus-9999999999-Hades"
# name = str1.split("-")[0]
# age = str1.split("-")[1]
# owner = str1.split("-")[2]
#
# dog3 = Dog(name, age, owner)

