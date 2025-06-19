from functools import reduce


# def functie1():
#     pass
#
# if 0 == 0:
#     print("yes")
# else:
#     pass

def functie2():
    return 2

print(functie2())

var1 = functie2

print(var1())
print(var1 is functie2)

lst1 = [0, 2, 4]
lst2 = [0, 2, 4]
lst1_copy = lst1

print(lst1 is lst1_copy)

print('--------------')

# Functii, Metode, Functii lambda.
# Metoda este o functie care apartine unei Clase.
# Functie Lambda este o functie fara nume, folosita o data sau de doua ori. Nu e refolosita la acelasi nivel cu functiile.

def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# 4 + (2 / 5) * (6 + 4) = ?

result = 4 + (2 / 5) * (6 + 4)
print(result)

result_functii = add(4, multiply(divide(2, 5), add(6, 4)))
print(result_functii)

print("------------------")

lst = [1000, 10, 15, 20, 35, 40, 100, 7, 9]

resultat = []
for nr in lst:
    resultat.append(nr * 2)

print(resultat)

# range(1000000)
# -> [0, 1, 2, 3, 4, ......., 999999]
# list(range(1000000))

def multiply_by_two(nr):
    return nr * 2

print(multiply_by_two(5))

multiplied = list(map(multiply_by_two, lst))
print("Multiplied")
print(multiplied)

multiplied2 = list(map(lambda x: x * 2, lst))
print(multiplied2)

# def even_number_check(nr):
#     if nr % 2 == 0:
#         return True
#     else:
#         return False

even_nrs = list(filter(lambda x: x % 2 == 0, lst))
print(even_nrs)

multiple_of_5 = list(filter(lambda x: x % 5 == 0, lst))
print(multiple_of_5)

# lst = [1000, 10, 15, 20, 35, 40, 100, 7, 9]
total = reduce(lambda x, y: x * 2 + y * 3, lst)
print(total)

# Multiply by two only even numbers, return only those numbers.

result2 = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, lst)))
print(result2)

filter_evens = filter(lambda x: x % 2 == 0, lst)
map_multiply_by_two = map(lambda x: x * 2, filter_evens)
result_of_mult = list(map_multiply_by_two)

print(result_of_mult)

print("------------------")

# zip

a = ['Zamfir', 'Ana', 'Maria', 'Matei', 'Luca']
b = [110, 24, 32, 18, 7]

unified = []

for i in range(len(a)):
    person = a[i]
    age = b[i]
    unified.append((person, age))

print(unified)

unified_zipped = list(zip(a, b))
print(unified_zipped)

lst3 = [5, 4, 10, 29, 200, 100, 13, 7, 31]
lst3.sort(reverse=True)
print(lst3)

# [('Luca', 7), ('Matei', 18)]
# v = ('Luca', 7)
# v[0] = 'Luca'
# v[1] = 7
# ('Luca', 7, 'Iasi', 3, 100, True)
# v[5] = True
# () -> {}
# ('Luca', 7, 'Iasi', 3, 100, True)
# { "Name": "Luca", "Age": 7, Bank_Balance: 100"}
# unified_zipped.sort(key=lambda x: x["Bank_Balance"])

unified_zipped.sort(key=lambda x: x[1])
print(unified_zipped)

lst_dict = [{
    "Name": "Zamfir",
    "Age": 110
}, {
    "Name": "Dan",
    "Age": 30
}, {
    "Name": "Matei",
    "Age": 15
}]

def what_key(p):
    return p["Age"]

lst_dict.sort(key=lambda x: x["Age"])
# lst_dict.sort(key=what_key)
print(lst_dict)


# Ex. 1: Creaza functii de calcul aritmetic, + - * /, add, subtract, etc, si efectueaza urmatoarele calcule:
# 100 - 300 + (7 * 80) / 2
# 7 - 8 + 3 * 4 / 10
# Inmulteste toate numerele de la 1 la 100

# Ex 2:
# Primind doua liste de date, de genul:
# [ 'Matei', 'Luca', 'Ana', 'Gabriel' ]
# [ 10, 20, 30, 15 ]
# Creaza o lista de dictionare, unde un element de dictionar arata:
# d = {
#     "Nume": "Matei",
#     "Varsta": 10
# }

# Ex 3:
# Primind lista: [10, 20, 80, 56, 2342, 5453, 7, 8 ,9]
# Folosind map(), ridica toate numerele la puterea a 2-a
# Creaza folosind filter() o lista cu toate nr pare din prima lista.


total = 1
for i in range(1, 101):
    total *= i

print(total)

# 100 - 300 + (7 * 80) / 2
# 7 - 8 + 3 * 4 / 10

r11 = subtract(100, add(300, divide(multiply(7, 80), 2)))
print(r11)


