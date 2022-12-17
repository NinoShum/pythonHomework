#Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint
list = []
for i in range(5):
    list.append(randint(0, 20))

print ("Начальный список: " + str(list))

from random import randint
for i in range(len(list)-1, 0, -1):
    j = randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 
print ("Перемешанный список: " +  str(list))

