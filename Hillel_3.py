# Урок 8.1. - Додати 1 до числа
def add_one(some_list):
    number = int(''.join(map(str, some_list)))
    number += 1
    return [int(digit) for digit in str(number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


# Урок 8.2 -  Паліандром

import string
def is_palindrome(text):
    filtered = ''.join(ch.lower() for ch in text if ch.isalnum())
    return filtered == filtered[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
