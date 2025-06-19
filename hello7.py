import random
import string
from datetime import datetime

v = 10

def change(param1):
    param1 = 200

print(v)
change(v)
print(v)


l1 = [10, 20]

def change_list(list1):
    list1.append(30)

print(l1)
change_list(l1)
print(l1)

d1 = {
    "name": "john",
    "age": 30
}

def change_dictionary(dict1):
    # mutable data structure
    dict1["employed"] = True
    # dict1.update(employed=True)

print(d1)
change_dictionary(d1)
print(d1)

# mutable data structures: list, dictionary, set,
l1 = [1, 2, 3]
l1.append(4)

# immutable data structures: string, tuple

# s1 = "python"
# s1[0] = 't'
# print(s1)

t1 = ("Brasov", 400000)
t2 = ("Iasi", 350000, True, "hundreds", "broken roads", "rust in the air")

# t2[2] = False

print(t1)
print(t2[3])

v = {
    "nav_button": "closed",
    "cookie_banner": "active",
    "post_list": ["Why has America gone so far with its overweight epidemic?", "Where do monocariotes come from?"],
    "user": "john",
    "users_active": 30432423
}

# v["nav_button"] = "opened"
# v = {
#     "nav_button": "opened",
#     "cookie_banner": "active",
#     "post_list": ["Why has America gone so far with its overweight epidemic?", "Where do monocariotes come from?"],
#     "user": "john",
#     "users_active": 30432423
# }


list2 = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 1, 2, 3]
set1 = set(list2)

print(len(set1))


list3 = []
for i in range(10000):
    list3.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

start = datetime.now()
print("ASDFG" in list3)
#  O(n)
print("Stop: {}".format((datetime.now() - start).microseconds))
# print(1 in list444)
# O(1)

set4 = set(list3)

start2 = datetime.now()
print("ASDFG" in set4)
# O(1) -> constant
print("Stop: {}".format((datetime.now() - start2).microseconds))


print(datetime.now().timestamp())
