import random


#Условия ввода
while True:
    num = int(input("Нечетное число: "))
    if num % 2 != 0 and num > 2:
        break
    else:
        print("Введите корректное число")

#Создание матрицы
matrix = [[random.randint(0, 9) for i in range(num)] for i in range(num)]

#Вывод матрицы на экран
for i in matrix:
    print(i)


minElement = matrix[0][num - 1]

for i in range(num):
    j = num - 1 - i
    if i != j:
        if matrix[i][j] < minElement:
            minElement = matrix[i][j]

# Вывод результата
print(f"Минимальный элемент: {minElement}")

a = [1, 2, 3]

