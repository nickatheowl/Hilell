print("Hello World")  #Урок1

number = int(input("Введіть 4-значне число: "))  #Урок2
digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10
print(digit1)
print(digit2)
print(digit3)
print(digit4)

number = int(input("Введіть 5-значне число: "))  #Урок3
d1 = number // 10000
d2 = (number % 10000) // 1000
d3 = (number % 1000) // 100
d4 = (number % 100) // 10
d5 = number % 10
reversed_number = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1
print(reversed_number)

num1 = float(input("Введіть перше число:"))  #Урок3.1
operation = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if operation == '+':
    result = num1 + num2
    print("Результат:", result)
elif operation == '-':
    result = num1 - num2
    print("Результат:", result)
elif operation == '*':
    result = num1 * num2
    print("Результат:", result)
elif operation == '/':
    if num2 == 0:
        print("Помилка: Ділення на нуль!")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Невідома операція!")

first_list = [1, 2, 3, 4, 5, 6]  #Урок3.2
first_list = first_list[-1:] + first_list[:-1]
print(first_list)

lst = [1, 2, 3, 4, 5]  #Урок3.3
middle = (len(lst) + 1) // 2
result = [lst[:middle], lst[middle:]]
print(result)
#або
first_list = [2, 4, 7, 11, 0, -2, 8]
new_list = [first_list[:4], first_list[4:]]
print(new_list)

first_list = [0, 1, 0, 12, 3]  #Урок4.1
first_list[:] = [x for x in first_list if x != 0] + [0] * first_list.count(0)
print(first_list)
#або
first_list = [0, 1, 0, 12, 3]
first_list[:] = list(filter(lambda n: n != 0, first_list)) + [0] * first_list.count(0)
print(first_list)

lst = [1, 3, 5]  #Урок4.2
i = 0
s = 0
while i < len(lst):
    s = s + lst[i]
    i = i + 2
result = s * lst[-1] if lst else 0
print(result)

lst = []
i = 0
s = 0
while i < len(lst):
    s = s + lst[i]
    i = i + 2
result = s * lst[-1] if lst else 0
print(result)

import random  #Урок 4.3
lst = [random.randint(1, 9) for _ in range(random.randint(3, 10))]
new_lst = [lst[0], lst[2], lst[-2]]
print(new_lst)


import string #Урок 5.1
import keyword

my_string = "pizza_time"

print(my_string)
print(type(my_string))

print(
    not keyword.iskeyword(my_string)
    and not (my_string.count('_') > 1 and all(c == '_' for c in my_string))
    and my_string != ''
    and not my_string[0].isdigit()
    and all(
        c not in string.punctuation.replace('_', '')
        and not c.isupper()
        and not c.isspace()
        for c in my_string
    )
)
