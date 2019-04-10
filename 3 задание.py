# -*- coding: utf-8 -*-
    
__author__ = 'Гайдуков Александр Михайлович'
print ('Задание 3')

x1 = int(input("введите координаты первой точи (x1): "))
x2 = int(input("введите координаты второй точи (x2): "))
k = int(input("введите коффициент(к): "))
b = int(input("введите параметр(b): "))
y1 = k*x1+b
y2 = k*x2+b
print (y1,y2)

from tkinter import *
window = Tk()
window.title('Работа с canvas')

canvas = Canvas(window,width=600,height=600,bg="gray", cursor="pencil")
canvas.create_line(x1,y1,x2,y2,width=5,fill="yellow")
canvas.pack()
window.mainloop()

