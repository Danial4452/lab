import math
import time

#Task 1 math.prod()
numbers = [12,34,5,2,352,13]
result = math.prod(numbers)
print("Произведение всех чисел",result)

#Task 2 isupper() islower()
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

text = "Kanye West"
upper, lower = count_upper_lower(text)
print(f"Заглавных букв: {upper}, Строчных: {lower}")


#Task 3 reversed()
s = "HellllNaaahhhhh"
reversed_s = "".join(reversed(s))
if s == reversed_s:
    print("Tes, its palindrome")
else:
    print("No")
    
#Task 4 time.sleep() sqrt()
def sqrt_after_delay(number, mls):
    delay_seconds = mls / 1000 
    time.sleep(delay_seconds)  
    return math.sqrt(number)

number = 49
mls = 200
result = sqrt_after_delay(number, mls)
print(f"Квадратный корень из {number} после {mls} миллисекунд: {result}")

#Task 5 all()
def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(f"элементы {tuple1} тру? {all_elements_true(tuple1)}")
print(f"элементы {tuple2} тру? {all_elements_true(tuple2)}")
    
