# tuple vs list
    # Iterating through a "Tuple" is faster than in a "list".
    # "Lists" are mutable whereas "Tuples" are immutable.
    # "Tuples" that contain immutable elements can be used as a ley for a dictionary.

# Reverse a tuple

'''
tuples = ('z','a','d','f','g','e','e','k')
output: ('k','e','e','g','f','d','a','z')

tuples = ('10','11','12','13','14','15')
output: ('15','14','13','12','11')

'''

input_tuple = ('z','a','d','f','g','e','e','k')
print("Input tuple",input_tuple)
list = []
for x in reversed(input_tuple):
    list.append(x)
output_tuple = tuple(list)
print("Reversed tuple: ",output_tuple)