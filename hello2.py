
var1 = {
    "Iasi": 300000,
    "Brasov": 250000,
    "Bucuresti": 2000000,
    "Cluj": 400000,
}

lista_echipa = ["Daniel", "Amalia", "Roman", "Alex", "Dragos"]

var2 = {
    "Echipa": lista_echipa
}

var3 = {
    "Dict2": {
        "Dict3": {
            "Dict4": {
                "Dict5": "Sfarsit"
            }
        }
    }
}

print(var1)
print(var1["Iasi"])
# Key: Value pairs

for k in var1:
    print(k)
    print(var1[k])


cetateni = {
    19304843895738: {
        "Nume": "Antochi Adrian",
        "Varsta": 32,
        "Adresa": "Brasov, Jud Brasov",
        "Greutate": 75,
        "Moldovean": True
    },
    193048438345345: {
        "Nume": "Remus Luca",
        "Varsta": 30,
        "Moldovean": False
    }
}


def verifica_moldovean(cnp):
    # verifica in baza de date de cetateni, daca cetateanul cu cnp-ul dat are valoarea de Moldovean egala cu True
    cetatean = cetateni[cnp]
    if cetatean["Moldovean"] == True:
        return True
    else:
        return False

# i = 0
# while True:
#     if i == 100000:
#         break
#     print(i)
#     i = i + 1

# Pornim o bucla infinta de cod
while True:
    print("Scrie un CNP de verificat in sistem, sau scrie 'stop' pentru a opri programul.")
    # primim text de la console
    text = input("Introduce CNP-ul cautat:")
    # verificam daca am scris 'stop' in console
    if text == "stop":
        # daca am scris stop, atunci oprim bucla folosind "break"
        print("Programul se opreste!")
        break

    # schimbam textul din string in int
    cnp_dat = int(text)

    print("Cetateanul cu cnp: ")
    print(cnp_dat)
    print("Este Moldovean?")

    try:
        # apelam functia care verifica in baza noastra de date daca persoana cu CNP-ul dat este Moldovean
        print(verifica_moldovean(cnp_dat))
    except KeyError as e:
        print("Nu exista cetateanul cu cnp-ul dat!")

