# coding: utf-8

# Задание №1

print ("Задание 1")
print ()

d = 1
q = input ("Что делаем хозяин? Дальше пытаем ПК - Y, Заканчиваем (ноль) - 0: ")
if q == 'Y':
    print ()
    print ("Посчитаем, друг мой")
    print ()
    x = int(input("Введите первое число = "))
    y = int(input("И второе число = "))
    if y == 0:
        y = int(input("Пожалуйста, поменяйте число, так как, введенное Вами равно 0: "))
    else:    
        while int(d) != 0:  
            answer = input("Введите операцию: 1 - сложение чисел, 2 - вычитание (x-y), 3 - деление (x/y): ")
            if answer == '1':
                z = x + y
                print (z)
            elif answer == '2':
                z = x - y
                print (z)
            elif answer == '3':
                z = x/y
                print (z)
            else:
                print ()
                print ("Вы ввели значение не из указанного диапазона! Жаль, конечно.")
                d = int(input ("Что делаем хозяин? Если продолжаем, то введите число от 1 до 3. Если заканчиваем - введите ноль (0): "))
else:
    print ("Пока, не забудьте закрыть двери :(")

# Задание №2

print()
print ("Задание 2*")
print ()

chet = 0
nchet = 0
x = input ("Введите любое натуральное число (например, 34398): ")
print ("Спасибо!")
n = len (x)
# print ("n = ", n)
# print (x[0])
i = 0
while i <= n-1:
    if int(x[i]) % 2 == 0:
        chet = chet + 1
    else:
        nchet = nchet + 1
    i += 1
print ("Четных чисел = ", chet)   
print ("Нечетных чисел = ", nchet)



# Задание №7
# Рекурсия

print()
print ("Задание 7*")
print ()

def rec1 (n):
    if n == 0:
        return 0
    else:
        return n + rec1(n - 1)

def rec2 (n):
    if n == 0:
        return 1
    else:
        return n * (n + 1)/2

n = int(input("Введите n = "))
print (F"Проверяем равняются ли n*(n + 1)/2 = и 1 + ..+ n. Итак, {rec1(n)} = {rec2(n)}. УРА!!!")
