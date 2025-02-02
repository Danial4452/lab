from some_func import converting, gradus, filter_prime 

grams = float(input("Скок граммов: "))
print("в унциях:", converting(grams))

fahrenheit = float(input("в Фаренгейтах: "))
print("В Цельсиях:", gradus(fahrenheit))

numbers = list(map(int, input("Вбейте числа: ").split()))
print("Простые числа из них:", filter_prime(numbers))





