
# Scrie un program care primeste de la consola un numar, il stocheaza in baza de date doar daca numarul este par.
# Afiseaza intreaga lista dupa fiecare rulare.
# Ruleaza programul pana scriem in baza de date 'stop'
# hint: foloseste .append(nr) ca sa adaugam numarul in baza de date

from tools import is_even

def run_program(numbers_list):
    text = input("Input number to check parity. Input 'stop' to stop program")
    if text == 'stop':
        return True

    nr = int(text)
    if is_even(nr):
        numbers_list.append(nr)

    return False

number_db = []

while True:
    do_we_stop = run_program(number_db)
    if do_we_stop:
        break
    print(number_db)




