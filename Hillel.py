print("Hello World")  #Урок1

number = int(input("Введіть 4-значне число: ")) #Урок2
digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10
print(digit1)
print(digit2)
print(digit3)
print(digit4)

number = int(input("Введіть 5-значне число: ")) #Урок3
d1 = number // 10000
d2 = (number % 10000) // 1000
d3 = (number % 1000) // 100
d4 = (number % 100) // 10
d5 = number % 10
reversed_number = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1
print(reversed_number)

num1 = float(input("Введіть перше число: ")) #Урок3.1
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


def move_last_to_front(lst): #Урок3.2
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]

print(move_last_to_front([12, 3, 4, 10]))
print(move_last_to_front([12, 3, 4, 10, 8]))


def split_list(lst): #Урок 3.3
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
