import math

#Task 1
def degrees_to_radians():
    degrees = float(input("Вонзи свой degree: "))
    radians = math.radians(degrees)
    print(f"Вот твои радианы: {radians:.6f}")
    #Градусы в радианы — как перевести градусы в 'пи-штуки'. Магия математики!

#Task 2. Площадь трапеции
def trapezoid_area():
    height = float(input("Высота: "))
    base1 = float(input())
    base2 = float(input())
    area = 0.5 * (base1 + base2) * height
    print(f"ОУТПУТ: {area}")
    #Трапеция — это как прямоугольник, но с дополнительной 'изюминкой'. Площадь считаем, как профи!

#Task 3. Площадь правильного многоугольника
def polygon_area():
    n = int(input("СКОК ИХ: "))
    side_length = float(input("Длиннннннннна: "))
    area = (n * side_length ** 2) / (4 * math.tan(math.pi / n))
    print(f"АРЕА ОВ ЗИС: {area}")
#Многоугольник — это как пицца, но с большим количеством кусочков. Площадь считаем, как настоящие математические гурманы!

#Task 4. Площадь параллелограмма
def parallelogram_area():
    base_length = float(input("длинна: "))
    height = float(input("высота parallelogram: "))
    area = base_length * height
    print(f"Output: {area}")
#Параллелограмм — это как прямоугольник, но с наклоном в сторону. Площадь считаем, не падая в обморок!

# Вызов функций
print("КОНВЕРТИНГ")
degrees_to_radians()

print("АРЕА")
trapezoid_area()

print("ПЛОЩАДЬ")
polygon_area()

print("ПАРАЛЛЕЛОГРАММА")
parallelogram_area()

#Вот и всё, задачи решены! Теперь можно расслабиться и запостить это в Instagram с хэштегом #MathIsLife.