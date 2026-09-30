'''
Given three arrays, we have to find common elements in three sorted lists using sets.
input: ar1 = [1,5,10,20,40,80]
       ar2 = [6,7,20,80,100]
       ar3 = [3,4,15,20,30,70,80,120]
output: [80,20]

input: ar1 = [1,5,5]
        ar2 = [3,4,5,5,10]
        ar3 = [5,5,10,20]
output: [5]
'''

ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

# Typecasting to make a set from array
s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

# Printing the sets
print(s1)
print(s2)
print(s3)

#Joining using intersection
'''
new_set = s1.intersection(s2) # s1 intersects with s2
final_set = new_set.intersection(s3)
print(final_set)

'''


new_final_set = s1.intersection(s2).intersection(s3)
print(new_final_set)

#Typecasting set into list
final_list = list(new_final_set)
print(final_list)

print("===================")
l1 = [1,5,20,10,5]
l2 = [3,4,5,20,5,10] 
l3 = [5,5,10,20]

set1 = set(l1)
set2 = set(l2)
set3 = set(l3)

print(set1)
print(set2)
print(set3)

# Intersecting a sets
new_set = set1.intersection(set2).intersection(set3)
print(new_set)

# Typecasting the set into a list
new_list = list(new_set)
print(new_list)