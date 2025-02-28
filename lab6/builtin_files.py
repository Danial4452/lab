import math

#Task 1
numbers = [12,34,5,2,352,13]
result = math.prod(numbers)
print("Произведение всех чисел",result)

#Task 2
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

text = "Kanye West"
upper, lower = count_upper_lower(text)
print(f"Заглавных букв: {upper}, Строчных: {lower}")




#Task 3
s = "HellllNaaahhhhh"
reversed_s = "".join(reversed(s))
if s == reversed_s:
    print("Tes, its palindrome")
else:
    print("No")
    
