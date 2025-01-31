#Task 1
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
        
