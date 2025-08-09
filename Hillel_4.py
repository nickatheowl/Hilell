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
