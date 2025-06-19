
s = "hello"
ss = 'hello'
vv = 'hello "world"'
v2 = "hello \"world\""

t1 = "hello \nworld"
par = "Lorem ipsum dolor sit amet consectetur adipiscing elit.\n Consectetur adipiscing elit quisque faucibus ex sapien vitae. \nEx sapien vitae pellentesque sem placerat in id. \nlacerat in id cursus mi pretium tellus duis. \nPretium tellus duis convallis tempus leo eu aenean."

t3 = "IOANA."
# 73 79 65 78 65
print(t3)
print(len(t3))
print(t3[0])
print(t3[-1])
print(t3.lower())

t4 = "Avem o propzitie care spune ceva sau altceva despre Ioana, o persoana dintr-un loc sau altul, nascuta intr-o familie cu 2 parinti."
print(t4.lower())
print(t4.upper())
print(t4.title())
print(t4.swapcase())
print(t4.title().swapcase())

t5 = " John Deere "
print(t5)

t5_cleaned = t5.strip()
print(t5_cleaned)

dirty_strings = [" Ana avea 60 de mere, dupa ce s-a intors de la piata.   .", " Ion avea 60 de mere, dupa ce s-a intors de la piata.        ."]


def clean_strings(strings):
    # removes whitespaces and extra punctuation marks from our strings
    result_list = []
    for s in strings:
        # [0, -1] returns a new string that is missing its last character.
        result_list.append(s[0:-1].strip())
    return result_list


print("Cleaning:")
c_strings = clean_strings(dirty_strings)
print(c_strings)
# t8 = " hello world       ."
# print(t8[0:-1].strip())

# print(vv)
# print(v2)
# print(t1)

terminal_input = "Adrian, Maria, Ion, Bula, Popescu"
print(terminal_input)
extracted_names = terminal_input.split(",")
cleaned_names = []
for s in extracted_names:
    cleaned_names.append(s.strip())
print(extracted_names)
print("Cleaned:")
print(cleaned_names)

t10 = "In programming an important part of it is learning about variables, functions, numbers, strings, etc. VariaBles are the building blocks of programming. Variables can store anything."

print(t10.lower().count("variables"))
if "programming" in t10:
    print("programming is in our string")
else:
    print("programming is not found in our string")

data_list = [10, 20, 30, 40, 50]
data_list2 = ["Hello", "World", "Space", "Earth"]
print(11 in data_list)
print("Earth" in data_list2)

joined_data = "-".join(data_list2)
print(joined_data)
split_t10 = t10.split("a")
print(split_t10)
joined_t10 = "z".join(split_t10)
print(joined_t10)

to_format = "{} are {} mere. Dupa ce a vandut {} a mai ramas cu {}".format("Ana", 50, 10, 50-10)
print(to_format)
to_format2 = "{persoana} are {} mere. Dupa ce a vandut {} a mai ramas cu {}".format(50, 10, 50-10, persoana="Ana")
print(to_format2)

name = "Maria"
fruit = "apples"

to_format3 = f"My name is {name} and I have 100 {fruit}."
print(to_format3)

# https://python-reference.readthedocs.io/en/latest/index.html
# https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage
# https://realpython.com/inheritance-composition-python/
# https://www.w3schools.com/python/python_inheritance.asp
