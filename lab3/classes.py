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