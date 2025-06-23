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

