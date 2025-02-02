#Task 1
import random


def converting(grams):
    return 28.3495231 * grams

if __name__ == "__main__":
    grams = float(input())  
    print(converting(grams))  
    
    
#Task 2
def gradus(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

if __name__ == "__main__":
    fahrenheit = float(input())  
    print(gradus(fahrenheit))  

#Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):  
        rabbits = numheads - chickens  
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None  

if __name__ == "__main__":
    numheads, numlegs = map(int, input().split())  
    result = solve(numheads, numlegs)
    if result:
        print(result[0], result[1])  
    else:
        print("No solution") #(Answer is 23 and 12)
        
        
#Task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers = list(map(int, input("Вонзи свои числа: ").split()))
print("Простые числа из них:", filter_prime(numbers))

#Task 5
def all_views(stroka, i=0):
    if i == len(stroka):
        print("".join(stroka))
        return  

    for j in range(i, len(stroka)):
        perm = list(stroka)
        perm[i], perm[j] = perm[j], perm[i]
        all_views(perm, i + 1)

all_views("USA")


#6

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

sentence = input("Вонзите ваше предложение: ")
print(reverse_words(sentence))


#7

def has_33(nums):

    check = ""
    for i in nums:
        check += str(i)


    if '33' in check:
        return True
    else:
        return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]), '\n')


#8


def spy_game(nums):
    check = []

    for i in nums:
        if i in [0,7]:
            check.append(i)

    if check == [0,0,7]:
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#9

def volume_of_sphere(r):

    cur = (4/3) * 3.1415 * r ** 3

    return f"Volume of Sphere with a {r} radius = {cur}\n"

print(volume_of_sphere(5))


#10

def uniq(nums):
    new = []

    for i in nums:
        if i not in new:
            new.append(i)


    return f"New version of list with only unique members: {new}"


print(uniq([52,69,66,44,44,52,44,44,88888]), '\n')


#11

def is_palindrome(stroka):

    check = [i for i in stroka if i not in [',', ' ','.']]

    if check == check[::-1]:
        return "Yes its a palindrome"
    else:
        return "No, its not a palindrome"

print(is_palindrome(input("Вонзите , какую строку вы хотите проверить: ")), '\n')


#12

def histogram(heigths):

    print(f"histogram for {heigths}:", '\n')

    for i in heigths:
        print('*' * i)
    print()


histogram([1,5,10])


#13


def game_for_life():
    tar = random.randint(1,21)

    print("Hello кбтушник !")


    att = 0

    while True:
        print("гадай.")

        cur = input()

        if not cur.isdigit():
            print("Ты че особенный?")
        elif int(cur) < tar:
            print("надо выше", '\n')
            att +=1
        elif int(cur) > tar:
            att += 1
            print("ниже", '\n')
        elif int(cur) == tar:
            print("г б ты прав",'\n')

            print(f"факапов: {att}")
            break


game_for_life()

        
