
# Задание - 2. Мой алгоритм
# 1-1, 2-3, 3-5, 4-7, 5-9, 6-11, 7-13, 8-15, 9-17

import cProfile

# ДО улучшения алгоритма - такие результаты:
# Введите i-ое по счёту простое число = 5
# Итак,  5 - ый по счету простой элемент = 9
# 536 function calls in 0.032 seconds

# АЛГОРИТМ - 1

def main (ni):
    n = 2
    i = 1
    d = {}
    print ()

    while i < ni:
        n += 1
        y = 1
        z = 0
        while y <= n//2:
            y += 1
            if n % y > 0:
                z += 1
            else:
                break
        if z > 0:
            i += 1
            d [i] = n
            # print ("i = ",i, "d[i] = ",d[i]," n = ",n," y = ",y)
    print ()                      
    print ("Итак, ",ni,"- ый по счету простой элемент =",d[i])
    print ()
ni = int(input("Введите i-ое по счёту простое число = "))
cProfile.run('main(ni)')

# 1-1, 2-3, 3-5, 4-7, 5-9, 6-11, 7-13, 8-15, 9-17

# АЛГОРИТМ - 2
# Введите i-ое по счёту простое число = 5
# Итак,  5 - ый по счету простой элемент = 9
# 438 function calls in 0.019 seconds

def main (ni):
    n = 2
    i = 1
    d = {}
    while i < ni:
        n += 1
        y = 1
        z = 0
        while y <= n//3:
            y += 1
            if n % y > 0:
                z += 1
            else:
                break
        if z > 0:
            i += 1
            d [i] = n                           
    print ("Итак, ",ni,"- ый по счету простой элемент =",d[i])
    print ()
ni = int(input("Введите i-ое по счёту простое число = "))
cProfile.run('main(ni)')
#print (main(ni))

