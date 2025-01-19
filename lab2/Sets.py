myset ={"Tokaev","Putin","Nazarbaev"}
#A set is a collection which is unordered, unchangeable, and unindexed.
#Sets inputing randomly positions and ignore duplicates


#Add set items
myset.add("Obama")
print(myset)

#Remove set items
myset.remove("Putin")
print(myset)

#Loop
for x in myset:
  print(x)
  
  
#Join of sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #or | sign of union
print(set3)

