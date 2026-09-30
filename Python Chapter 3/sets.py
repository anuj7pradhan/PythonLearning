# Container for storinng multiple values in a variable

# names = {"Anuj","Anjal","Prativa"}

# Set items
    # Unordered
    # Immutable -> cannot update existinng values, but can remove, add
    # Unindexed
    # Duplicates not allowed
    # Any datatypes
    # Mix of different data types

sets = {"Anjal","Prativa","Anuj"}
print(sets)
print(len(sets)) #Check length of set
print(type(sets)) #checking datatype

# accessing items of sets
for x in sets:
    print(x)

#check if an item exists in a set
if "Bhanu" in sets:
    print("Bhanu is in a sets.")
else:
    print("Bhanu is not available in a set.")

if "Anuj" in sets:
    print("Anuj is in a sets.")
else:
    print("Anuj is not available in a set.")

# Add element in a set
sets.add("Anuj") #duplicate values not allowed
print(sets)

sets.add("Hakim") #new item added
print(sets)

sets_list = ["Surya","Chandra","Hawa"]
sets.update(sets_list) #Updating the sets by adding new names in a list
print(sets)

#Removing a name
sets.remove("Hakim")
print(sets)

sets.remove("Hawa")
print(sets)


#Joining two sets

set1 = {"a","b","c","d","2"}
set2 = {"1","2","3","4"}
print(set1,set2)

new_set = set1.union(set2)
print(new_set)

set1.update(set2)
print(set1)

# keep duplicate values only (Intersection)
food1 = {"Pizza","hotdogg","Sandwitch","Chopsey"}
food2 = {"Pizza","Daal","Sandwitch","Bhat","Tarkari"}
food1.intersection_update(food2)
print(food1)

#Keep all values except duplicates
food1.symmetric_difference_update(food2)
print(food1)