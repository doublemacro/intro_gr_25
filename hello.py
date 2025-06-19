
v = 1000 + 300 + 100

variabila_2 = 100
variabila_3 = 200

total = v + variabila_2 + variabila_3
print(total)

v1 = 5
v2 = 2

print(v1 // v2)

list1 = [2, 4, 6, 10, 300, "a", 'adrian', "marian", 'julien "france"' , False]

print(list1)

telefoane = ["Galaxy A16", "Iphone 15x", "Huawei 300 pro"]
telefoane.append("One Plus 3T")

print(telefoane)


def adauga_element(param1):
    v = 100
    print(v)
    v = v + param1
    print(v)

adauga_element(30)


lista_a = [1, 3, 5, 7, 9]
lista_b = [2, 4, 6, 8, 10]

lista_rezultat = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(lista_rezultat)

# print(lista_ciudata)
# lista_ciudata_exemplu = [2, 3, [4, 5, 6]]

lista_exemplu = [100, 200, 300, 50, "a", True]
#                  0    1    2   3    4     5
lista_ciudata = [1, 3, 5, 7, 9]


# print(lista_exemplu[0])
# print(len(lista_exemplu))

for i in range(len(lista_ciudata)):
    lista_exemplu.append(lista_ciudata[i])

print(lista_exemplu)

tt1 = 10
if tt1 < 10:
    print("tt1 mai mica decat 10")
elif tt1 == 10:
    print("tt1 este 10")
else:
    print("tt1 mai mare decat 10")

# if True:
#     print("Hello")

lista_nr_comparare = [0, 2, 4, 5, 6, 7, 8, 10, 100, 2000, 2342345343463]
lista_nr_comparare[8]
lista_nr_comparare[-1]

for i in range(len(lista_nr_comparare)):
    nr = lista_nr_comparare[i]
    if nr % 2 == 0:
        print("Nr nostru {} este par!".format(nr))
    else:
        print("Nr nostru {} este impar!".format(nr))


def inmulteste_cu_doi(un_nr):
    rezultat = un_nr * 2
    return rezultat

r1 = inmulteste_cu_doi(30)
print(r1)
print(inmulteste_cu_doi(30))


def extrage_nr_pare(lista1):
    lista_noua = []
    for i in range(len(lista1)):
        nr = lista1[i]
        if nr % 2 == 0:
            lista_noua.append(nr)
    return lista_noua


nr_extrase = extrage_nr_pare(lista_nr_comparare)
print(nr_extrase)

