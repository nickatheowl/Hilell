#Урок 10.1 - Генераторна функція

def tag_decorator(tag1, tag2):
    def actual_decorator(func):
        def inner_wrapper(*func_args, **func_kwargs):
            print(f"Теги декоратора: {tag1}, {tag2}")
            result = func(*func_args, **func_kwargs)
            print("Функція виконана успішно")
            return result
        return inner_wrapper
    return actual_decorator

@tag_decorator("важливо", "терміново")
def greet_veronika(username):
    print(f"Привіт, {username}!")

greet_veronika("Вероніка")

#Урок 10.2. Знайти перше слово
def first_word(text):
    for ch in ".,":
        text = text.replace(ch, " ")
    words = text.split()
    return words[0] if words else ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

#Урок 10.3. Перевірити чи є парним чи ні

def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число """
    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
