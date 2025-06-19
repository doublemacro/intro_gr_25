
# Write a program that receives from the console the following input:
# 1923234234,Adrian,32
# Save this data to a list of people with cnp, name, age.

list1 = []
example_man = {
    "CNP": 1923234234,
    "Name": "Adrian",
    "Age": 32
}

while True:
    input_text = input("Input data, format: 1923834234,Adrian,32 \n")
    print(input_text.split(","))
    cnp, name, age = input_text.split(",")
    # cnp = input_text.split(",")[0]
    # name = input_text.split(",")[1]
    # age = input_text.split(",")[2]
    # "Adrian,32" -> ["Adrian", "32"]

    result_person = {
        "CNP": cnp,
        "Name": name,
        "Age": age
    }

    list1.append(result_person)

    for pers in list1:
        print(pers)






