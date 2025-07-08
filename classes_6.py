# Un atribut cu o singura talpa este Protected, si poate fi accesat din clasa in care e definit si din orice clasa care mosteneste clasa initiala. Atributul cu o singura talpa poate fi accesat si din afara clasei, dar nu este recomandat.
# Un atribut cu doua talip, de ex: self.__name, poate fi accesat din clasa in care este definit, si atat. O clasa care mosteneste clasa initiala nu are acces la acel atribut, si nici nu poate fi accesat din exteriorul clasei.


class Animal:
    def __init__(self, weight, name):
        Animal._validate_weight(weight)
        self._weight = weight
        self._name = name

    class StringWeightException(Exception):
        pass
    class KgInWeightException(Exception):
        pass
    class PositiveIntWeightException(Exception):
        pass

    @staticmethod
    def _validate_weight(weight: str):
        # weight = "10kg"
        # Don't allow negative numbers, don't allow space between number and 'kg', don't allow anything other than 'kg' as a measuring unit.
        if type(weight) != str:
            raise Animal.StringWeightException("Weight attribute needs to be of type 'str'!")
        if 'kg' not in weight:
            raise Animal.KgInWeightException("Weight attribute needs to contain 'kg' as a measuring unit!")
        # "axbxcxd".split('x') -> ["a", "b", "c", "d"]
        # "10kg".split('kg') -> ["10"]
        # weight[0:-2] -> "10"
        # v1 = int("10") -> 10, type(v1) -> int
        weight_as_int = int(weight[0:-2])
        if weight_as_int <= 0:
            raise Animal.PositiveIntWeightException("Weight must be a number grater than 0!")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        Animal._validate_weight(value)
        self._weight = value

    # Encapsulare:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


    def make_sound(self):
        print("{}: BluuruurB!".format(self._name))


anim1 = Animal("10kg", "Max")
anim1.make_sound()
# print(      anim1.name()     )
print(      anim1.name     )
anim1.name = "Shadow"

print(      anim1.name     )
# del anim1.name
# print(anim1.name)

# v1 = "909999090kg"
# print(v1[0:-2])

anim1.weight = "10kg"
print(anim1.weight)


# try catch:
print("-----------")
var1 = "10gr"

try:
    var1_as_int = int(var1)
    var1_as_int = var1_as_int + 1
    print(var1_as_int)

except ValueError as exc1:
    # code that runs if int() conversion fails.
    if "kg" in var1:
        var1_processed = var1[0:-2]
        var1_as_int = int(var1_processed)
        var1_as_int = var1_as_int + 1
        print(var1_as_int)

    var1 = 10
    print(var1 + 1)

# info_from_db_weight = "3ton"
info_from_db_weight = 30

try:
    anim2 = Animal(info_from_db_weight, "Elephant")

except Animal.KgInWeightException as ex1:
    correct_weight = int(info_from_db_weight[0:-3]) * 1000
    correct_weight_info = "{}kg".format(correct_weight)
    anim2 = Animal(correct_weight_info, "Elephant")
except Animal.StringWeightException as ex2:
    correct_weight = "{}kg".format(info_from_db_weight)
    anim2 = Animal(correct_weight, "Elephant")


print(anim2.weight)

print("----------")


class SimpleClass:
    def __init__(self, initial_list=None):
        if initial_list is None:
            initial_list = []
        self.stored_list = initial_list

    def simple_add_method(self, param1=0):
        self.stored_list.append(param1)


cls1 = SimpleClass()
cls1.simple_add_method(10)
print(cls1.stored_list)

cls2 = SimpleClass()
cls2.simple_add_method(20)
print(cls2.stored_list)

print(cls1.stored_list)


class Student:
    def __init__(self, grade):
        self.grade = grade

class Academy:
    def __init__(self):
        self._students = []

    def add_student(self, stud):
        self._students.append(stud)

    def select_top_students(self):
        result = []
        for student in self._students:
            if student.grade > 8:
                result.append(student)
        return result

        # result = [x for x in self._students if x.grade > 8]
        # return result

        # result = list(filter(lambda x: x.grade > 8, self._students))
