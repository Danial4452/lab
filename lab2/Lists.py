rappers = ["Kendrick Lamar", "Kanye West","Playboi Carti"]
print(rappers)
print(len(rappers))
print("The absolute GOAT is - " + rappers[0])

if "Playboi Carti" in rappers:
    print("SEEE YAAH")
    
rappers.insert(3,"Frank Ocean") #or we can use append
print(rappers)

#extend is for adding two lists into one

#loops:
for i in range(len(rappers)):
    print(i+1,rappers[i])

#(or we can use while)

#names with letter a
names = ["Danial", "Madina", "Diana", "Nurik", "Steve"]
newlist = []

for x in names:
  if "a" in x:
    newlist.append(x)

print(newlist)

#sorting
rappers.sort()
print(rappers)

#we can use keys in sorts
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#we also have reverse function
thislist.reverse()
print(thislist)

#copy
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#Join List
list3 = list1 + list2
print(list3)




    






