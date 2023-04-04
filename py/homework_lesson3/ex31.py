#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

from random import randint
list = []
for i in range(5):
    list.append(randint(-20, 20))

print (f"Начальный список: {list}")

summ = 0
for i in range(1, len(list), 2):
        summ += list[i]       
print(f"Cумма элементов на нечётных позициях: {summ}")