# -*- coding: utf-8 -*-
    
__author__ = 'Гайдуков Александр Михайлович'
print ('Задание 4')

import random

print()
x1 = int(input("Первая граница диапазона (x1): "))
x2 = int(input("Вторая граница диапазона (x2): "))
y = random.randint(x1, x2)

print()
print("случайное целое число",y)
print("случайное вещественное число", random.uniform(x1, x2))

print()

symbol = ['A','B','C','D','E','F','G','H','I','J','K',
           'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

random.shuffle(symbol)
print(symbol)     
random_symbol = random.choice(symbol)
print(random_symbol)

