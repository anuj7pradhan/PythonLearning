#Adding elements to a list

# append()
# insert()
# extend()

list_num = [1,2,3,33,4,6]
list_a = ["a","b","c","d"]
print(list_num)

# append()
list_num.append(8) #Adding item in a list
print(list_num)

# insert()
list_num.insert(4,77) # 4 is the index and 77 is the value to be inserted
print(list_num)

# extend()
list_a2 = ["e","f","g"]
list_a.extend(list_a2)
print("This is the new extended list",list_a)

