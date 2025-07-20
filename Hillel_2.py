import string
import keyword

my_string = input("I like pizza")

print(my_string)
print(type(my_string))

print(
    (my_string != '') and
    (not my_string[0].isdigit()) and
    (my_string == my_string.lower()) and
    (all((c not in string.punctuation or c == '_') and not c.isspace() for c in my_string)) and
    (my_string not in keyword.kwlist) and
    (my_string.count('_') <= 1) and
    (not (set(my_string) == {'_'} and len(my_string) > 1))
)
