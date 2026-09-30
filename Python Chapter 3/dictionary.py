# Dictionary -> key value pairs

# Dictionary Items
    # Ordered
    # Changeable
    # Unindexed
    # Duplicates not allowed
    # Any datatype

dic = {"name:anuj,age:33"}
print(dic)

ph_num = {
    "Anuj":9876,
    "Anjal": 65768,
    "Prativa":3423
}
print(ph_num)

#Checking type of dict
print(type(ph_num))

#Checking the length of the dict
print(f"There are {len(ph_num)} ph_numin the givendictionary.")

#Access items of dict 
print(ph_num["Anuj"])
print(ph_num.get("Anuj"))

# Updating value of the 
ph_num["Anuj"] = 234
print(ph_num)
print(ph_num["Anuj"])

# print the keys of the dict
print(ph_num.keys())

#Add elements in the dict
ph_num["Pantee"]=123423
print(ph_num)

#Adding more dictionary and updating
more_ph = {
    "sam":75656,
    "ram":21342
}

# Updating dictionary
ph_num.update(more_ph)
print(ph_num)

# Removing element

ph_num.pop("ram")
print(ph_num) 
ph_num.popitem()
print(ph_num) 

# Empty the dict
'''ph_num.clear()
print(ph_num)'''


# Printing elements of the dict
for x in ph_num.items():
    print(x)

for x,y in ph_num.items():
    print(x,y)

# Nested Dictionary

ph_num = {
    "Area1" :{
        "a":12,
        "b": 123,
        "c": 1234
    },
    "Area2":{
        "d":121,
        "e": 1231,
        "f": 12341
    }
}
print(ph_num["Area1"]["c"])
print(ph_num["Area2"]["e"])
