# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

Quarter = int(input("Введите четверть: "))
if 1 <= Quarter <=4:
    if Quarter == 1:
        print("X > 0")
        print("Y > 0")
    if Quarter == 2:
        print("X < 0")
        print("Y > 0")
    if Quarter == 3:
        print("X < 0")
        print("Y < 0")
    if Quarter == 4:
        print("X > 0")
        print("Y < 0")
else:
    print("Такой четверти нет")