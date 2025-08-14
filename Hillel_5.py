#Урок 11.1 - Генератор простих чисел
def prime_generator(end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for number in range(2, end + 1):
        if is_prime(number):
            yield number


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


#Урок 11.2 - Заповнення списку кубами чисел

def generate_cube_numbers(end):
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'


#Урок 11.3 - Перевірка на парність

def is_even(number):
    return (number & 1) == 0

print(is_even(10))
print(is_even(7))
print(is_even(0))
print(is_even(12345678901234567890))
print(is_even(12345678901234567891))

#Урок 12.1 - Очистити текст від html-тегів
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned_text = re.sub(r'<.*?>', '', html)
    cleaned_lines = [line.strip() for line in cleaned_text.split('\n') if line.strip()]
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(cleaned_lines))

# Приклад:
delete_html_tags('draft.html', 'cleaned.txt')


#Урок 12.2 - Корзина для покупок
class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # {Item: count}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {count} pcs."
                              for item, count in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())


# Приклад
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print("Total:", cart.get_total())  # 60

cart.add_item(apple, 10)  # тепер 20 + 10 = 30
print(cart)
print("Total:", cart.get_total())  # 80
