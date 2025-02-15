#Task 1
def squares_up_to_n(N):
    for i in range(N + 1):  
        yield i ** 2  # Ключевое слово которое делает функ. генератором


N = 5
for square in squares_up_to_n(N):
    print(square)
    

#Task 2
n = int(input())

def even_nums(n):
    for i in range(0, n + 1, 2):  
        if n != i:
            yield f"{i},"
        else:
            yield f"{i}"

for even in even_nums(n):
    print(even, end="") #Красивенько выводим на кондициях

    
#Task 3
def divisible(L):
    for i in range(L+1):
        if(i%3==0 and i%4==0):
            yield i

L = 100
for vikings in divisible(L):
    print(vikings)
    
#Task 4
def squares(a, b):
    for i in range(a, b + 1): 
        yield i ** 2  

a = 3
b = 7

for square in squares(a, b):
    print(square)
    
#Task 5
def countdown(n):
    while n >= 0:  
        yield n  
        n -= 1  

n = 5

for number in countdown(n):
    print(number)



