thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Since tuples are indexed, they can have items with the same value


#One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Access in tuple same like in lists

#Cause tuples are unchangable, we need to make them to lists 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#we already have a packed tuple, but we can unpack them 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits1 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits1

print(green)
print(tropic)
print(red)

#We also can use loops like in lists
#join tuples are the same with lists

#Tuple Methods
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

