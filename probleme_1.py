# https://leetcode.com/problemset/
# https://www.reddit.com/r/Python/comments/1knw7z/python_interview_questions/
# https://www.github.com/search/
# https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



def two_sum(number_list, target):
    for i in range(len(number_list)):
        nr1 = number_list[i]

        for j in range(i + 1, len(number_list)):
            nr2 = number_list[j]

            if nr1 + nr2 == target:
                return [i, j]


nums = [5, 6, 10, 30, 45]
target = 36

result = two_sum(nums, target)
print(result)



# Ex 2:

# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

# 224565422
# 1234321
# 99800899
# 353
# aghjhga
# oopoo
# ()(((()(
# ((()))


def check_palindrome(number: int):
    # 0 -> 9
    # 1 -> 8
    t = str(number)
    flag = True
    for i in range(len(t) // 2):
        char1 = t[i]
        index2 = len(t) - 1 - i
        char2 = t[index2]
        print("Checking ({} == {})".format(char1, char2))
        if char1 != char2:
            flag = False

    return flag

# print(check_palindrome("2245665422"))
# print(check_palindrome("10099344"))
# print(check_palindrome("224505422"))
print(check_palindrome(70955907))



# 303
# r = 3
# 30
# a = 3

# 30
# r = 0
# 3
# a = 30

# 3
# r = 3
# 0
# a = 303


variable_for_app = 10
VariableForApp = 1
VARIABLEFORAPP = 1
VARIABLE_FOR_APP = 1

v1 = 10

def func_1(x):
    x = 200

print(v1)
func_1(v1)
print(v1)

v2 = [1, 20, 3]

def func_2(x):
    x.append(400)

print(v2)
func_2(v2)
print(v2)






