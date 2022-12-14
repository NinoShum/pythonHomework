# Напишите программу для. проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


X = []
for i in range(3):
        X.append(int(input("Введите значение: ")))
print(X)
left = not (X[0] or X[1] or X[2])
right = not X[0] and not X[1] and not X[2]

if left == right:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")