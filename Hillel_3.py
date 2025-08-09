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

#Урок 8.3. - Унікальне число

def find_unique_value(some_list):
    for num in some_list:
        if some_list.count(num) == 1:
            return num

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")


#Урок 9.1. Визначити популярність певних слів у тексті

def popular_words(text, words):
    text_lower = text.lower().split()
    result = {}
    for word in words:
        result[word] = text_lower.count(word)
    return result

assert popular_words(
    '''Жабки стрибали по листочках, жабки співали під місяцем, жабки мріяли про літа. Жабка стрибала з кумедним дзвінким кваканням!''',
    ['жабки', 'місяцем', 'літа', 'жабка']
) == {'жабки': 3, 'місяцем': 1, 'літа': 1, 'жабка': 1}, 'Test1'
print('OK')

#Урок 9.2 - Різниця між числами
def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
