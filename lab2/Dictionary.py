thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Using the dict() method to make a dictionary
me = dict(name = "Danial", age = 18, country = "Kz")
print(me)

#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x,"is the model of the car")
#Or method "get()"

#keys
k = thisdict.keys()
print(k)
#value
v = thisdict.values()
print(v)

#The items() method will return each item in a dictionary, as tuples in a list.
item = thisdict.items()
print(item)

#Change with simple way or:
thisdict.update({"year": 2020})

#Remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Loops 
for x in thisdict.keys(): #or values and whatever u want
  print(x)
  
#Copy with copy() or dict()
mydict = dict(thisdict)
print(mydict)

#Nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])


#Loop of nested dict **
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

