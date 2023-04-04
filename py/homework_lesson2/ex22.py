# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.

number = int(input('Введите число последовательности: '))
#num = int(input('Введите начальное число последовательности: '))
result = []
sum = float()


for i in range(1, number + 1):
    result.append((1 + (1/i))**i)

for i in range(number):
    sum += result[i]
    result[i] = round(result[i], 2)


sum = round(sum, 2)
print(f'N = {number}:', end = " ")
print(result, sep = ', ')
print(f'Сумма {sum}')

