#Task 1
class StringProcessor:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

if __name__ == "__main__":
    sp = StringProcessor()
    sp.getString()
    sp.printString()


#Task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(self.length ** 2)

if __name__ == "__main__":
    length = int(input())
    square = Square(length)
    square.area()
    
#Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.length * self.width)

if __name__ == "__main__":
    length, width = map(int, input().split())
    rectangle = Rectangle(length, width)
    rectangle.area()
    
#Task 4
class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def show(self):
        return f"coordinates: x = {self.x}, y = {self.y}"

    def move(self):
        print("Choose how to change the coords:")
        print("x,y ->", end=": ")

        self.x, self.y = [int(i) for i in input().split(',')]

        
        print(f"Coords was successfully changed to {self.x}, {self.y}")
        

    def dist(self, point):

        q = (point.x - self.x) ** 2
        w = (point.y - self.y) ** 2

        e = (q + w) ** 0.5
        return f"Dist between two points equals to: {e}"

a = Point(0,0)
b = Point(1,1)

print(a.show())
print(b.show())

a.move()

print(a.show())
print(b.show())

print(a.dist(b))


#Task 5
class Account:

    owner = input("Your name: ")
    balance = 0

    def deposit(self,amount_of_money):
        Account.balance += amount_of_money
        print()
        print(f"{amount_of_money} was added to your balance.")
        print(f"Your current balance: {Account.balance}")

        print()

    def withdraw(self,amount_to_take):

        if amount_to_take <= Account.balance:
            print("Successfully !, good luck :D", f"{amount_to_take} was taken from your balance.")
            Account.balance -= amount_to_take
            print()
            print(f"Your current balance: {Account.balance}")
            print()
        else:
            print()
            print("Oops!, your current balance is less than you want to take !")
            print()
            print(f"Your current balance: {Account.balance}, but you want to take {amount_to_take}.")


kbtu = Account()

kbtu.deposit(5000)
kbtu.withdraw(2500)
kbtu.withdraw(5000)
print()

#Task 6

def is_prime(n):

    if n == 1 or n < 2: return False

    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

nums = [int(i) for i in range(50)]


ans = list(filter(lambda x: is_prime(x), nums))

print(ans)
