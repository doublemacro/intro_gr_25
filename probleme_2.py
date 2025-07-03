#        1152921504606846975
# nr16 = 0xFFFFFFFFFFFFFFF # -> 15 * 16^0 + 15 * 16^1 -> 15 + 240 -> 255
# nr2 = 215 # -> 5 * 10^0 + 1 * 10^1 + 2 * 10^2
# print(nr16)


class Bucket:
    def __init__(self, arg1):
        self.number = arg1


nr1 = 10

def func_1(arg1: Bucket):
    # changed bucket1 number value from 100 to 9999
    arg1.number = 9999
    # no change to bucket1 variable
    # arg1 = Bucket(888)

bucket1 = Bucket(50)
print(bucket1.number)
bucket1.number = 100
print(bucket1.number)

func_1(bucket1)
print("After modification")
print(bucket1.number)


# list comprehension:

# list_orig = [0, 1, 2, 3, 4, 5]
# [0, 6) -> 0, 0.00000000000001, 0.00000000002,....., 0.5999999999999.....
list_orig = range(6)
list_secundara = []
for x in list_orig:
    r = x * 2
    list_secundara.append(r)

print(list_secundara)

list_t = [x*2 for x in range(6)]
print(list_t)

# list_to_filter = [0, 39, 20, 120, -23, -434, 99, -100, 1]
# filtering_result = []
#
# for x in list_to_filter:
#     if x >= 0:
#         filtering_result.append(x)
#
# print(filtering_result)

list_to_filter = [0, 39, 20, 120, -23, -434, 99, -100, 1]
filtering_result = [x for x in list_to_filter if x >= 0]
print(filtering_result)

# list_t = [x*2 for x in range(6)]
dict_1 = {"{} to the power of 2".format(x): x**2 for x in range(6)}
print(dict_1)

