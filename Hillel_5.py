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
