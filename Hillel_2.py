# Урок 7.1 -  Вітання
def hello_user(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


print(hello_user("Veronika", 32))


# Урок 7.2 -  Модифікувати рядок
def correct_sentence(text):
    text = text.strip()
    if not text:
        return '.'
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')


# Тест 1
text = "greetings, friends"
if not text:
    result = '.'
else:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    result = text
print(result)

# Тест 2
text = "hello"
if not text:
    result = '.'
else:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    result = text
print(result)

# Тест 3
text = "Greetings. Friends"
if not text:
    result = '.'
else:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    result = text
print(result)
