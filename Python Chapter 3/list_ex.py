'''
Given a list in python and provided the index of the elements, 
write a program to swap the two elements in the list.

Ex:
input: list = [2,6,1,9], idx1 = 0, idx2 = 2
output: [1,6,2,9]
'''

'''
n = int(input("Enter size of the list: "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)
idx1 = int(input("Enter index1:"))
idx2 = int(input("Enter index2:"))
print(list)
#Swapping values at  idx1 and idx2
temp= list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)   
'''


n = int(input("Enter the size of the list: "))
list = []
for _ in range(n):
    num = int(input("Enter list item: "))
    list.append(num)
idx1 = int(input("Enter index 1: "))
idx2 = int(input("Enter index 2: "))
print("List made: ",list)

temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print("Swapped list: ",list)
